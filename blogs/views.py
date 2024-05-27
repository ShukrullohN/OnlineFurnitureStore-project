from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel
class BlogListView(ListView):
    template_name="blogs/blog-list.html"
    context_object_name = 'blogs'
    model = BlogModel
    paginate_by = 2



    def get_context_data(self, *, object_list=None, **kwargs):
        blogs = BlogModel.objects.all()
        cat = self.request.GET.get('cat')
        if cat:
            blogs = blogs.filter(categories__in=cat)
    
        context = {
            'blogs' : blogs,
            'categories': BlogCategoryModel.objects.all(),
            'tags' : BlogTagModel.objects.all(),
            'famous_blogs':  BlogModel.objects.all().order_by('-created_at'),
        }
        return context

class BlogDetailView(DetailView):
    template_name= 'blogs/blog-detail.html'
    context_object_name='blog'
    model = BlogModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'categories': BlogCategoryModel.objects.all(),
            'blog': BlogModel.objects.get(pk=self.kwargs['pk']),
            'tags' : BlogTagModel.objects.all(),
            'famous_blogs':  BlogModel.objects.all().order_by('-created_at'),
            'releted_blogs': BlogModel.objects.filter(categories__in=self.objects.categories.all())[:3]
        }
        return context