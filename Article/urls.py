from django.conf.urls import patterns, url

urlpatterns = patterns("",
        url(r"^add/$", "Article.views.articleAdd"),
        )