from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="blog/blog.html")),
              url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="blog/post.html"))
              ]
# ?P corresponds to named groups, do see once
#<pk>--primary key every post gets one;;;starts from 0 and is auto incrementing
#\d corresponds to digit in regular expression