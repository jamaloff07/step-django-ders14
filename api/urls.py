from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:category_id>/", views.category_detail, name="category_detail"),
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/<int:tag_id>/", views.tag_detail, name="tag_detail"),
    path("stats/", views.stats, name="stats"),
]
