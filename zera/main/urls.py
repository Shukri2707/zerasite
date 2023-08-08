from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('services/', views.services, name='services'),
    path('createfeedback/', views.create_fb, name='createfb'),
    path('contacts/', views.contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
