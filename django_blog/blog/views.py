from django.shortcuts import redirect, render, get_object_or_404
from .forms import CustomUserCreateForm
from django.contrib.auth import login,logout
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Post, Comment, Tag
from django.http import HttpResponseForbidden
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from  django.db.models import Q

#view to handle user registration and login
def register(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #login a user after succesfull login
            return redirect('post-list')
    else:
        form = CustomUserCreateForm()
    return render(request, 'blog/register.html', {'form': form})

#view for profile management
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    else:
        return render(request, 'blog/profile.html', {'user': request.user})

#custom logout view
def custom_logout(request):
    logout(request)
    return redirect('login')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def is_admin(user):
        return user.is_staff

class PostCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    context_object_name = 'post-create'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set logged-in user as author
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in to perform this action.")
        if not request.user.is_superuser:  # or any other role condition
            return HttpResponseForbidden("You do not have permission to perform this operation!")
        return super().dispatch(request, *args, **kwargs)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You don't have permissions to Update!")
        return super().dispatch(request, *args, **kwargs)
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    fields = ['title', 'content']
    success_url = '/post/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You don't have permission to Delete")
        return super().dispatch(request, *args, **kwargs)

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blog/comment_form.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk'] 
        return super().form_valid(form)
    
    #method to dynamically generate success url with the post's pk
    def get_success_url(self):
        return reverse_lazy('comment-list', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])  
        return context

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'   

    #filtering comments by post id
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])  # Add post to context
        return context

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content', 'author']
    template_name = 'blog/comment_update.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author 

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author #only authors can delete
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])  # Adds post to context
        return context

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[self.tag])  #filter posts by tag
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context
    
def posts_by_tag(request, tag_name):
    posts =  Post.objects.filter(tag__name__iexact=tag_name)
    return render(request, 'blog/post_detail.html', {'posts': posts, 'tag_name': tag_name})

def search_results(request):
    query = request.GET.get('q', '')
    results = Post.objects.none()

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct()

    return render(request, 'blog/search_results.html', {'posts': results, 'query': query})