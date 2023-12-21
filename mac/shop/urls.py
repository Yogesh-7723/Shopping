from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='contact'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('ProductView/',views.ProductView,name='productView'),
    path('checkout/',views.checkout,name='Checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
