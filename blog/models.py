from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

GPU_BRAND = ((0, "NVIDIA"), (1, "AMD"), (2, "OTHER"))

ADD_GPU_BRAND = ((0, "NVIDIA"), (1, "AMD"))

MEMORY_SIZE = ((0, "4GB"), (1, "8GB"), (2, "12GB"), (3, "16GB"), (4, "20GB"), (5, "24GB"), (6, "48GB"))  # noqa


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")  # noqa
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    sourced_from = models.URLField(max_length=255, blank=True, verbose_name="Image Sourced From")  # noqa

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    # Save function taken from https://www.benchatronics.com/detail/how-to-use-slug-and-populate-slug-outsude-django-admin  # noqa
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class GPU(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="GPU Name")  # noqa
    gpu_brand = models.IntegerField(choices=ADD_GPU_BRAND, default=0, verbose_name="Brand")  # noqa
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField(verbose_name="GPU Information")
    sourced_from = models.URLField(max_length=255, blank=True, verbose_name="Content Sourced From")  # noqa
    memory_size = models.IntegerField(choices=MEMORY_SIZE, default=0, verbose_name="Memory Size")  # noqa
    memory_type = models.CharField(max_length=10, verbose_name="Memory Type")
    base_clock = models.SmallIntegerField(default=0, verbose_name="Base Clock (MHz)")  # noqa
    boost_clock = models.SmallIntegerField(default=0, verbose_name="Boost Clock (MHz)")  # noqa
    specs = models.TextField(blank=True, verbose_name="Other Specs")
    date_released = models.DateField(default=date.today, verbose_name="Date Released")  # noqa
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created On")  # noqa
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Updated On")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Status")  # noqa

    class Meta:
        ordering = ['-date_released']

    def __str__(self):
        return self.name

    # Save function taken from https://www.benchatronics.com/detail/how-to-use-slug-and-populate-slug-outsude-django-admin  # noqa
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(GPU, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # noqa
    name = models.CharField(max_length=80)
    email = models.TextField()
    body = models.TextField()
    brand = models.IntegerField(choices=GPU_BRAND, default=2, verbose_name="Current GPU")  # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
