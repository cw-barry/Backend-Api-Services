"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Backend Services API",
        default_version="v1",
        description="Backend Services for many applications",
        terms_of_service="#",
        contact=openapi.Contact(email="barry@clarusway.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(
        cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path('menu/', include('menu.urls')),
    path('image/', include('images.urls')),
    path('opentripmap/', include('opentripmap.urls')),
    path('product/', include('products.urls')),

    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('todo/',include('todo.urls')),
    path('simple_todo/',include('simple_todo.urls')),
    path('contacts/',include('contacts.urls')),
    path('student/',include('students.urls')),
    path('practice/',include('practice.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)