from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Post, GPU
from .forms import CommentForm, GPUForm, PostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.template import loader
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView  # noqa

"""
List view ti display all posts excluding drafts.
"""


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


"""
List view to display all posts including drafts. Must be logged in.
"""


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')  # noqa
class AdminPostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        """
        If user is not a superuser raise a 403 custom error page
        """
        if not self.request.user.is_superuser:
            messages.error(request, 'DENIED: User is not an admin.')
            raise PermissionDenied
        return super().get(request, *args, **kwargs)


"""
View to show the Post detail template with approved comments.
"""


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            }
        )


"""
View for adding and removing likes for the user
"""


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


"""
Default list view for GPUs. Does not display drafts.
"""


class GPUList(ListView):
    model = GPU
    template_name = "gpu.html"
    paginate_by = 8
    queryset = GPU.objects.filter(status=1).order_by("-date_released")


"""
List view to display all GPUs including drafts. Must be logged in.
"""


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')  # noqa
class AdminGPUList(ListView):
    model = GPU
    template_name = "gpu.html"
    paginate_by = 8
    queryset = GPU.objects.order_by("gpu_brand", "-date_released")

    def get(self, request, *args, **kwargs):
        """
        If user is not a superuser raise a 403 custom error page
        """
        if not self.request.user.is_superuser:
            messages.error(request, 'DENIED: User is not an admin.')
            raise PermissionDenied
        return super().get(request, *args, **kwargs)


"""
List view to only display AMD GPUs
"""


class AMDList(ListView):
    model = GPU
    queryset = GPU.objects.filter(gpu_brand=1).filter(status=1).order_by("-date_released")  # noqa
    template_name = "gpu.html"
    paginate_by = 8


"""
List view to only display Nvidia GPUs
"""


class NVIDIAList(ListView):
    model = GPU
    queryset = GPU.objects.filter(gpu_brand=0).filter(status=1).order_by("-date_released")  # noqa
    template_name = "gpu.html"
    paginate_by = 8


"""
Default view for GPU Detail
"""


class GPUDetail(DetailView):
    model = GPU
    template_name = "gpu_detail.html"


"""
Create view to add a new GPU to the list. Must be logged in.
"""


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')  # noqa
class AddGPU(CreateView):
    model = GPU
    form_class = GPUForm
    template_name = "add_gpu.html"

    def get(self, request, *args, **kwargs):
        """
        If user is not a superuser raise a 403 custom error page
        """
        if not self.request.user.is_superuser:
            messages.error(request, 'DENIED: User is not an admin.')
            raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Upon form success prompt the user with a message
        """
        messages.success(self.request, "GPU Sucessfully created.")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        """
        View the related GPU
        """
        return reverse_lazy("gpu_detail", args=[str(self.object.slug)])


"""
Create view to add a new post to the list. Must be logged in.
"""


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')  # noqa
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def get(self, request, *args, **kwargs):
        """
        If user is not a superuser raise a 403 custom error page
        """
        if not self.request.user.is_superuser:
            messages.error(request, 'DENIED: User is not an admin.')
            raise PermissionDenied

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Upon form success prompt the user with a message
        """
        form.instance.author = self.request.user
        messages.success(self.request, "Post Sucessfully created.")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        """
        View the related post
        """
        return reverse_lazy("post_detail", args=[str(self.object.slug)])


"""
Update view to edit existing GPU data. Must be logged in.
"""


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')  # noqa
class UpdateGPU(UpdateView):
    model = GPU
    form_class = GPUForm
    template_name = 'update_form.html'

    def get(self, request, *args, **kwargs):
        """
        If user is not a superuser raise a 403 custom error page
        """
        if not self.request.user.is_superuser:
            messages.error(request, 'DENIED: User is not an admin.')
            raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Upon form success prompt the user with a message
        """
        messages.success(self.request, "GPU Sucessfully updated.")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        """
        View the related GPU
        """
        return reverse_lazy("gpu_detail", args=[str(self.object.slug)])


"""
Update view to edit existing post data. Must be logged in.
"""


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')  # noqa
class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_form.html'

    def get(self, request, *args, **kwargs):
        """
        If user is not a superuser raise a 403 custom error page
        """
        if not self.request.user.is_superuser:
            messages.error(request, 'DENIED: User is not an admin.')
            raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Upon form success prompt the user with a message
        """
        messages.success(self.request, "Post Sucessfully updated.")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        """
        View the related post
        """
        return reverse_lazy("post_detail", args=[str(self.object.slug)])


"""
Delete view to delete exisiting GPU data. Must be logged in.
"""


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')  # noqa
class DeleteGPU(DeleteView):
    model = GPU
    template_name = 'delete_gpu.html'

    def get(self, request, *args, **kwargs):
        """
        If user is not a superuser raise a 403 custom error page
        """
        if not self.request.user.is_superuser:
            messages.error(request, 'DENIED: User is not an admin.')
            raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        """
        Display success message and return to GPU list
        """
        messages.success(self.request, "GPU Sucessfully deleted.")
        return reverse_lazy("gpu")


"""
Delete view to delete exisiting post data. Must be logged in.
"""


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')  # noqa
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'

    def get(self, request, *args, **kwargs):
        """
        If user is not a superuser raise a 403 custom error page
        """
        if not self.request.user.is_superuser:
            messages.error(request, 'DENIED: User is not an admin.')
            raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        """
        Display success message and return to home page
        """
        messages.success(self.request, "Post Sucessfully deleted.")
        return reverse_lazy("home")


"""
Custom view for 403 errors
"""


class Error403(TemplateView):
    template_name = '403.html'


"""
Custom view for 404 errors
"""


class Error404(TemplateView):
    template_name = '404.html'


"""
Custom view for 500 errors
"""


class Error500(TemplateView):
    template_name = '500.html'
