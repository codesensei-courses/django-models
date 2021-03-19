from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import debug_toolbar

urlpatterns = [
    path('', TemplateView.as_view(template_name="store/index.html"), name="index"),
    path('store/', include('store.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)), # Debug toolbar
]