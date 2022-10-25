from django.urls import path, include

from exam_feb_2022.my_music.views import home_page, add_album,\
    album_details, edit_album, delete_album, profile_details, delete_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:album_id>/', album_details, name='album details'),
        path('edit/<int:album_id>/', edit_album, name='edit album'),
        path('delete/<int:album_id>/', delete_album, name='delete album'),
    ])),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
