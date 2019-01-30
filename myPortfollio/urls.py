from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
import jobs.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home,name='home'),
    path('blog/',include('blog.urls'))
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
