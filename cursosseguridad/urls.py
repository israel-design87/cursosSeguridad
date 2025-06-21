"""
URL configuration for cursosseguridad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from cursos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('', views.root_redirect, name='root'),
    path('signin/', views.signin, name='signin'),
    path('presentation/delete/<int:presentation_id>/', views.delete_presentation, name='delete_presentation'),
    path('checkout/', views.crear_checkout, name='crear_checkout'),
      path('pago_exitoso/', views.pago_exitoso, name='pago_exitoso'),  # <-- Esta línea es la clave
    path('pago_cancelado/', views.pago_cancelado, name='pago_cancelado'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('registro_cancelado/', views.registro_cancelado, name='registro_cancelado'),
    path('inicio/', views.inicio, name='inicio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)