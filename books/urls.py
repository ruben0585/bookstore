from django.urls import path
from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'), #la dirección será '' ya que quiero que la lsta de libros aparezca en el home
]