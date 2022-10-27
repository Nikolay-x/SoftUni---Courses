from django.urls import path

from exam_jun_2021.web.views import home_page, add_note, edit_note, \
    delete_note, note_details, profile_page, delete_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('add/', add_note, name='add note'),
    path('edit/<int:note_id>/', edit_note, name='edit note'),
    path('delete/<int:note_id>/', delete_note, name='delete note'),
    path('details/<int:note_id>/', note_details, name='note details'),
    path('profile_page/', profile_page, name='profile page'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
