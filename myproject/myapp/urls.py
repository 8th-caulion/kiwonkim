from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

import myapp.views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', myapp.views.main, name="main"),
    path('profile/', myapp.views.profile, name="profile"),
    path('req/', myapp.views.req, name="req"),
    path('req/<int:req_id>', myapp.views.detail, name="detail"),
    path('new/', myapp.views.new, name="new"),
    path('req/create', myapp.views.create, name="create"),
    path('req/edit/<int:req_id>', myapp.views.edit, name="edit"),
    path('req/update/<int:req_id>', myapp.views.update, name="update"),
    path('req/delete/<int:req_id>', myapp.views.delete, name="delete"),
]
