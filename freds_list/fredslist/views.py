from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from rest_framework.authtoken.models import Token
from fredslist.models import State, City, Post, Category, SubCategory, Favorite
from fredslist.forms import PostForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


# send_mail("Your Subject", "This is a simple text email body.","Yamil Asusta <cesarm2333@gmail.com>", ["cesarwebdevelopment@gmail.com"])
# send_mail("Your Subject", "This is a simple text email body.","Yamil Asusta <cesarwebdevelopment@gmail.com>", ["cesarm2333@gmail.com"])


################     SHARED MAIN SITE VIEWS   ##########################
class StateList(ListView):
    model = State
    template_name = 'fredslist/shared/post_list.html'
    # queryset = State.objects.order_by('-city')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.all()
        return context


class CityDetail(DetailView):
    model = City

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        context['category'] = Category.objects.all()
        return context


# class CategoryList(ListView):
#     model = Category
#     queryset = Category.objects.order_by('title')
#     slug_field = "username"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['subcategory'] = SubCategory.objects.all()
#         # context['city'] = get_object_or_404(City,pk=self.kwargs['city_name'])
#         context['city'] =get_object_or_404(City,city=self.kwargs['city_name'])
#         return context


class PostList(ListView):
    model = Post
    template_name = 'fredslist/post/post_list.html'
    paginate_by = 5
    queryset = Post.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        context['favorites'] = Favorite.objects.all()
        return context


def create_favorite(request, post_id):
    post = Post.objects.get(id=post_id)
    #   send_mail("Your Subject", "This is a simple text email body.",
    # "Yamil Asusta <hello@yamilasusta.com>", ["cesarwebdevelopment@gmail.com"])

    if Favorite.objects.filter(post__id=post_id, user__id=request.user.id).exists():
        return HttpResponseRedirect(reverse('home'))

    Favorite.objects.create(user=request.user, post=post)
    return HttpResponseRedirect(reverse('post_list'))


class MyPostList(ListView):
    model = Post
    template_name = 'fredslist/fredslist_admin/admin.html'
    queryset = Post.objects.order_by('-created_at')

    def get_queryset(self):
        return Post.objects.filter(user__username=self.request.user.username).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user.username
        context['user_token'] = Token.objects.filter(user=self.request.user)
        context['page_load'] = timezone.now()
        return context


class TopPostList(ListView):
    model = Post
    template_name = 'fredslist/post/topposts.html'
    # queryset = Favorite.objects.order_by('-favorited_at')
    # queryset = Favorite.objects.annotate(num_favorites=Count('post__id')).order_by('num_favorites')


    def get_queryset(self):
        # return Favorite.objects.annotate(num_favorites=Count('post__id')).order_by('num_favorites')
        return Post.objects.all().annotate(fav_count=Count('favorite')).order_by('-fav_count')

        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     context['user'] = self.request.user.username
        #     context['page_load'] = timezone.now()
        #     return context


################     POST CRUD   ##########################
class CreatePost(CreateView):
    model = Post
    form_class = PostForm

    template_name = 'fredslist/post/post_create.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class PostDetail(DetailView):
    model = Post
    template_name = 'fredslist/post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('list_bookmarks')
    template_name_suffix = '_update_form'


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('list_bookmarks')


class PostSearch(ListView):
    model = Post
    template_name = 'fredslist/post/postsearch_list.html'

    def post_search(request, search):
        posts = Post.objects.filter(posting_title__icontains=search)
        return HttpResponseRedirect(reverse('post_list'))

    def get_queryset(self):
        return Post.objects.all().annotate(fav_count=Count('favorite')).order_by('-fav_count')


# def post_search(request, search):
#     posts = Post.objects.filter(posting_title__icontains=search)
#     return HttpResponseRedirect(reverse('post_list'))

def search(request):

    posts = request.POST['search_field']
    search_posts = Post.objects.filter(posting_title__icontains=posts)

    return render_to_response('fredslist/post/postsearch_list.html', {'posts': search_posts})





























# with open('states.csv', 'r') as f:
# read_data = f.readlines()
# input_state = read_data[0]



#     for input_city in range(1, len(read_data)):
#     reader = list(csv.reader(f, delimiter=',', skipinitialspace=True))
#

#     input_state = reader[0]
#     State.objects.create(state=input_state)
#     for input_city in range(1, len(reader)):
#       City.objects.create(city=input_city, state = input_state)




# import csv
# with open('states.csv', 'r') as f:
#      reader = csv.reader(f, delimiter=',')
#      for row in reader:
#          input_state = row[0]
#          new_state = State.objects.create(state=input_state)
#
#          for input_city in range(1, len(row)):
#                  City.objects.create(city=row[input_city], state = new_state)


# import csv
# with open('categories.csv', 'r') as f:
#      reader = csv.reader(f, delimiter=',')
#      for row in reader:
#          input_category = row[0]
#          new_category = Category.objects.create(title=input_category)
#
#          for input_subcategory in range(1, len(row)):
#                  SubCategory.objects.create(title=row[input_subcategory], category = new_category)
