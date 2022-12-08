
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from .forms import PostForm, CommentForm
from .models import Post, Comment


@method_decorator(cache_page(10), 'dispatch')
class AllPostView(generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        posts = Post.objects.select_related('owner').filter(is_published=True)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_edit_page'] = True
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_edit_page'] = True
        return context


class PostDetailOpenView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_edit_page'] = False
        return context


class CommentListView(generic.ListView):
    model = Comment
    template_name = 'blog/commentlist.html'
    paginate_by = 2

    def get_queryset(self):
        posts = Comment.objects.filter(post__id=self.kwargs.get('pk'), is_published=True)
        return posts


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = PostForm
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


@method_decorator(cache_page(10), 'dispatch')
class UsersPostView(generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        posts = Post.objects.select_related('owner').filter(owner=self.request.user, is_published=True)
        return posts


class NotPublishedView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        posts = Post.objects.select_related('owner').filter(owner=self.request.user, is_published=False)
        return posts


class CreatePostsView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    form_class = PostForm
    login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreatePostsView, self).form_valid(form)


class CreateCommentView(generic.CreateView):
    model = Comment
    template_name = 'blog/create_comment.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog:post_detail_open', kwargs={'pk': self.object.post.pk})

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs.get('pk'))
        form.instance.post = post
        return super(CreateCommentView, self).form_valid(form)




