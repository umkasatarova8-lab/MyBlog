from django.urls import path
from .views import PostListView, PostDetailView # Импортируем наши Views

urlpatterns = [
    # Главная страница (список постов)
    path('', PostListView.as_view(), name='post-list'),

    # Страница одного поста
    # <int:pk> - это "захват" части URL. Django возьмет число из URL,
    # назовет его 'pk' (Primary Key) и передаст в DetailView.
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
