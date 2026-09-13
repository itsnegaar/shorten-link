from django.urls import path
from short_links.views import RetriveShortLinksView, CreateShortLinksView


urlpatterns = [
    path('resolve', RetriveShortLinksView.as_view()),
    path('shrink', CreateShortLinksView.as_view()),
]