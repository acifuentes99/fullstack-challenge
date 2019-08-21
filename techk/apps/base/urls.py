from django.urls import include, path
from rest_framework import routers
import apps.base.views as views

app_name = "base"

router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet)
router.register(r'categories', views.CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/category/<category>', views.BooksByCategory.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
