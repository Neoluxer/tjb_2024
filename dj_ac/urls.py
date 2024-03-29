"""
URL configuration for dj_ac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import commercial_offer.views
import customer.views
import make_contract_base.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', customer.views.home, name='home'),
                  path('result/', commercial_offer.views.result, name='result'),
                  path('offer/', commercial_offer.views.offer, name='offer'),
                  path('contract/',include('make_contract_base.urls')),
                  path('result_contract/', make_contract_base.views.result_contract, name='result_contract'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
