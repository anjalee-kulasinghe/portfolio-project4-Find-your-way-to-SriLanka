from django.urls import path, include
from .views import Index, BlogView, DetailArticleView, LikeArticle, Featured, DeleteArticleView, add_comment


urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('cityguide/', include('cityguide.urls')),
    path('food/', include('food.urls')),
    path('traveltips/', include('traveltips.urls')),
    path('blog/', BlogView.as_view(), name='blog'),
    path('article/<int:pk>/add_comment/', add_comment, name='add_comment'),
]