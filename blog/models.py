from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

GPU_BRAND = ((0, "NVIDIA"), (1, "AMD"), (2, "OTHER"))

ADD_GPU_BRAND = ((0, "NVIDIA"), (1, "AMD"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class GPU(models.Model):
    name = models.CharField(max_length=200, unique=True)
    brand = models.IntegerField(choices=ADD_GPU_BRAND, default=0)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    specs = models.TextField(blank=True)
    date_released = models.DateField(default=date.today)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="gpu_likes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    # https://www.benchatronics.com/detail/how-to-use-slug-and-populate-slug-outsude-django-admin


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.TextField()
    body = models.TextField()
    brand = models.IntegerField(choices=GPU_BRAND, default=2)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

