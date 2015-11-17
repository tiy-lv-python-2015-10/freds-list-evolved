import logging
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from rest_framework.authtoken.models import Token
from peteslist.forms import ForSaleForm, ImageForm, SearchForm, KeywordForm
from peteslist.models import Location, Category, Post, Favorite, Keyword
from django.utils import timezone
from django.db.models import Q, Count

logger = logging.getLogger(__name__)


class LocationList(ListView):
    model = Location

    def dispatch(self, request, *args, **kwargs):
        """
        Check session for location. If there, redirect to city. If not,
          go to home directory.
        :param request: session.location
        :param args:
        :param kwargs:
        :return:
        """
        city = self.request.session.get('location')
        return HttpResponseRedirect(reverse('temp_only',
                                            kwargs={'city': city}))

    def get_context_data(self, **kwargs):
        """
        Separate states into 4 lists.
        :param kwargs:
        :return:
        """
        state_list = []
        context = super().get_context_data(**kwargs)
        for location in Location.objects.all():
            if location.state not in state_list:
                state_list.append(location.state)
        context['page_load'] = timezone.now()
        context['states1'] = state_list[0:13]
        context['states2'] = state_list[13:26]
        context['states3'] = state_list[26:39]
        context['states4'] = state_list[39:]
        return context


class LocationListHome(ListView):
    """ This is a repeat model for a home link with no session check"""
    model = Location
    template_name = 'peteslist/location_home.html'

    def get_context_data(self, **kwargs):
        """
        Separate states into 4 lists.
        :param kwargs:
        :return:
        """
        state_list = []
        context = super().get_context_data(**kwargs)
        for location in Location.objects.all():
            if location.state not in state_list:
                state_list.append(location.state)
        context['page_load'] = timezone.now()
        context['states1'] = state_list[:13]
        context['states2'] = state_list[13:26]
        context['states3'] = state_list[26:39]
        context['states4'] = state_list[39:]
        return context


def loc(request, city):
    """
    Render to city requested. Separate categories into 10 lists.
    Add city to session.
    :param request:
    :param city:
    :return:
    """
    city_list = []
    for location in Location.objects.all():
        city_list.append(location.city)

    if city not in city_list:
        return HttpResponseRedirect(reverse('locs_list'))

    community1 = Category.objects.filter(type__title='community')[:7]
    community2 = Category.objects.filter(type__title='community')[7:]
    housing = Category.objects.filter(type__title='housing')
    for_sale1 = Category.objects.filter(type__title='for sale')[:19]
    for_sale2 = Category.objects.filter(type__title='for sale')[19:]
    services1 = Category.objects.filter(type__title='services')[:10]
    services2 = Category.objects.filter(type__title='services')[10:]
    jobs = Category.objects.filter(type__title='jobs')
    gigs1 = Category.objects.filter(type__title='gigs')[:4]
    gigs2 = Category.objects.filter(type__title='gigs')[4:]
    context_dict = {'community1': community1, 'community2': community2,
                    'housing': housing, 'for_sale1': for_sale1,
                    'for_sale2': for_sale2, 'services1': services1,
                    'services2': services2, 'jobs': jobs,
                    'gigs1': gigs1, 'gigs2': gigs2, 'city': city}
    request.session['location'] = city

    return render(request, 'peteslist/category_list.html', context_dict)


class ForSalePost(View):
    """ Renders home page to Create Post """
    def get(self, request):
        form = ForSaleForm()
        return render(request, 'peteslist/post.html', {'form': form})

    def post(self, *args, **kwargs):
        form = ForSaleForm(self.request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = self.request.user
            locate = self.request.session['location']
            post.location = Location.objects.get(city=locate)
            post.save()
            self.request.session['post_id'] = post.id

            return HttpResponseRedirect(reverse('add_image'))

        return render(self.request, 'peteslist/post.html', {'form': form})


def add_image(request):
    """
    Add image to Post
    :param request:
    :return:
    """
    ImageFormSet = formset_factory(ImageForm, extra=5)
    if request.method == 'POST':
        formset = ImageFormSet(request.POST, request.FILES)
        post_id = request.session.get('post_id')
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    image = form.save(commit=False)
                    if image.image:
                        image.post = \
                            Post.objects.get(id=post_id)
                        image.save()
        return HttpResponseRedirect(reverse('post_detail',
                                            args=(str(post_id),)))
    else:
        formset = ImageFormSet()
    return render(request, 'peteslist/add_image.html', {'formset': formset})


class ListPosts(ListView):
    model = Post
    paginate_by = 10

    def post(self, catch):
        """
        Add search words to a get url
        :param catch: unused parameter
        :return: HttpResponse with search querystring
        """
        if self.request.method == 'POST':
            form = SearchForm(self.request.POST)
            if form.is_valid():
                search = form.cleaned_data['search']
                return HttpResponseRedirect(reverse('list_posts') +
                                            '?search=' + search)
            else:
                return HttpResponseRedirect(reverse('list_posts'))

    def get_queryset(self):
        """
        Query for post list to return. Location is required. Check for other
        filters including order by top50 most favorited, sort by price, and
        Search words.
        :return: filtered post list
        """
        location = self.request.session.get('location')
        posts = Post.objects.filter(location__city=location)\
            .order_by('-created_at')
        category = self.kwargs.get('category', None)
        if category:
            posts = posts.filter(category__title=category)
        top50 = self.request.GET.get('top50')
        if top50:
            posts = posts.annotate(fav_count=Count('favorite')).\
                order_by('-fav_count')
        sort = self.request.GET.get('sort')
        if sort == 'priceasc':
            posts = posts.order_by('price')
        if sort == 'pricedesc':
            posts = posts.exclude(price=None)
            posts = posts.order_by('-price')
        search = self.request.GET.get('search')
        if search:
            search = search.split()
            q_list = [Q(title__icontains=word) for word in search]
            q_list2 = [Q(description__icontains=word) for word in search]
            q_list = q_list + q_list2
            query = q_list.pop()
            for item in q_list:
                query |= item
            posts = posts.filter(query)
        return posts

    def get_context_data(self, **kwargs):
        """
        Appends one image per post if available.
        Adds Search form to be rendered
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        posts = Post.objects.filter(location__city=self.
                                    request.session.get('location'))
        category = self.kwargs.get('category', None)
        if category:
            posts = posts.filter(category__title=category)
        images = []
        for post in posts:
            if post.image_set.all():
                images.append(post.image_set.all()[0])
        context['images'] = images
        form = SearchForm()
        context['form'] = form
        logger.debug("*********ERROR************")
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        """ Adds image_set """
        context = super().get_context_data(**kwargs)
        b = self.object.image_set.all()
        context['images'] = b
        return context


def add_favorite(request, post_id):
    """
    Create favorite object linked to User and Post.
    Only add if not favorited yet.
    :param request:
    :param post_id:
    :return:
    """
    user = request.user
    post = Post.objects.get(id=post_id)
    for favorite in user.favorite_set.all():
        if favorite.post.id == int(post_id):
            return HttpResponseRedirect(reverse('list_posts'))

    Favorite.objects.create(user=user, post=post)
    return HttpResponseRedirect(reverse('list_posts'))


def delete_favorite(request, post_id):
    """
    Delete favorited post
    :param request:
    :param post_id:
    :return:
    """
    user = request.user
    post = Post.objects.get(id=post_id)
    fav = Favorite.objects.get(post=post, user=user)
    if fav:
        fav.delete()
    return HttpResponseRedirect(reverse('list_posts'))


class UserAccount(ListView):
    model = Post
    template_name = 'peteslist/user_account.html'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        """ Checks if user is logged in. There is a better way to do this
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not self.request.user.id:
            return HttpResponseRedirect(reverse('list_locations'))
        return super().dispatch(request, *args, **kwargs)

    def post(self, catch):
        """
        Form to add Keyword objects for user. Separates words and adds an
        object for each.
        :param catch: useless
        :return:
        """
        if self.request.method == 'POST':
            form = KeywordForm(self.request.POST)
            if form.is_valid():
                keywords = form.cleaned_data['keywords']
                keyword_list = keywords.split()
                for keyword in keyword_list:
                    Keyword.objects.create(user=self.
                                           request.user, keyword=keyword)
                return HttpResponseRedirect(reverse('account'))
            else:
                return HttpResponseRedirect(reverse('account'))

    def get_queryset(self):
        """ get user posts """
        user_posts = Post.objects.filter(user__username=self.request.user.
                                         username).order_by('-created_at')
        return user_posts

    def get_context_data(self, **kwargs):
        """
        Add form for keywords.
        Add images for posts.
        Add token key for user.
        Add keyword list if they have any.
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        try:
            token_key = Token.objects.get(
                user__username=self.request.user.username).key
        except Exception as e:
            return HttpResponseRedirect(reverse('list_locations'))
        context['key'] = token_key
        posts = Post.objects.filter(
            location__city=self.request.session.get('location'))
        images = []
        for post in posts:
            if post.image_set.all():
                images.append(post.image_set.all()[0])
        context['images'] = images
        form = KeywordForm
        context['form'] = form
        keywords = Keyword.objects.filter(user=self.request.user)
        if keywords:
            context['keywords'] = keywords
        return context


def regenerate_token(request):
    user = User.objects.get(username=request.user.username)
    token = Token.objects.get(user=user)
    token.delete()
    Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('account'))


def delete_keyword(request, keyword_id):
    keyword = Keyword.objects.get(id=keyword_id)
    keyword.delete()
    return HttpResponseRedirect(reverse('account'))
