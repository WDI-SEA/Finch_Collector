
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='index'),
    path('', include('second_app.urls')),
    path('cats/', include('library.urls')),
    path('owner/', include('library.urls'))
]
