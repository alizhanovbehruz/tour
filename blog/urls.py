from django.urls import path

from blog.views import home, filter_tick, about, packk, hotels, contact, pack_show

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('packages/',packk, name='packages'),
    path('aviatick/',hotels, name='hotels'),
    path('aviatick-search/', filter_tick, name='ticket_page'),
    path('contact/',contact, name='contact'),
    path('packages/<int:post_id>/',pack_show, name='tour_'),
]