from django.urls import path, include
from rest_framework import routers

from cinema.views import GenreListView, ActorListView, ActorDetailView, GenreDetailView, MovieViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreListView.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre_detail"),
    path("actors/", ActorListView.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor_detail"),
    path("cinemahalls/", ActorListView.as_view(), name="cinemahalls_list"),
    path("cinemahalls/<int:pk>/", ActorDetailView.as_view(), name="cinemahalls_detail"),
    path("", include(router.urls))
]

app_name = "cinema"
