from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from fredslist.models import State, City, Post, Category, SubCategory
from fredslist.forms import PostForm


class StateList(ListView):
    model = State
    # queryset = State.objects.order_by('-city')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.all()
        return context


class CategoryList(ListView):
    model = Category
    queryset = Category.objects.order_by('title')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.all()
        return context


class PostList(ListView):
    model = Post
    template_name = 'fredslist/my_post_list.html'
    paginate_by = 5
    queryset = Post.objects.order_by('-created_at')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context



class MyPostList(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_at')

    def get_queryset(self):
       return Post.objects.filter(user__username=self.request.user.username).order_by('-timestamp')

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['page_load'] = timezone.now()
       return context



class PostDetail(DetailView):
    model = Post



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





class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('list_bookmarks')
    template_name = 'fredslist/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


