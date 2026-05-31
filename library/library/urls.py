from django.urls import include, path
from author.views import author_view
from book.views import book_view
from order.views import order_view
from user.views import user_view

urlpatterns = [
    path('author/', author_view, name='author'),
    path('book/', book_view, name='book'),
    path('order/', order_view, name='order'),
    path('user/', user_view, name='user'),
]