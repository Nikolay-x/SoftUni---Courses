from django.urls import path, re_path

from exam_aug_2021.web.views import home_page, add_book, edit_book, book_details, \
    profile_page, edit_profile, delete_profile, delete_book

urlpatterns = (
    path('', home_page, name='home page'),
    path('add/', add_book, name='add book'),
    path('edit/<int:book_id>/', edit_book, name='edit book'),
    path('details/<int:book_id>/', book_details, name='book details'),
    path('profile', profile_page, name='profile page'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('delete/<int:book_id>', delete_book, name='delete book'),
)
