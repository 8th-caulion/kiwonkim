from django.contrib import admin
from django.urls import path, include
import myapp.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio")
]
