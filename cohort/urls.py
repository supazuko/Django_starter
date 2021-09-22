from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.cohort, name='cohort'),
    path('fetch', views.fetch, name='fetch'),
    path('native/', views.native, name='native'),
    path('create_native/', views.create_native, name='create_native'),
    path('create_cohort/', views.create_cohort, name='create_cohort'),
    # path('cohort', ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)