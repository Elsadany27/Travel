"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from bus import views
from rest_framework.authtoken.views import obtain_auth_token
#from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="API Documentation",
   ),
   public=True,
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('mixins_list',views.mixins_list.as_view()),
    path('mixins_pk/<int:pk>',views.mixins_pk.as_view()),
    path('mixins_list_reservation',views.mixins_list_reservation.as_view()),
    #filter reservation
    path('detailsreservation',views.detailsreservation),

    #bus
    path('mixins_list_bus',views.mixins_list_bus.as_view()),
    path('mixins_pk_bus/<int:pk>',views.mixins_pk_bus.as_view()),
    path('searchbus',views.searchbus),

    #get token
    path('gettoken',obtain_auth_token)
]
