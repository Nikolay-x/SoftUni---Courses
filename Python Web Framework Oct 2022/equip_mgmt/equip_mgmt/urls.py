"""equip_mgmt URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('equip_mgmt.api.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('equip_mgmt.accounts.urls')),
    path('pumps/', include('equip_mgmt.pumps.urls')),
    path('certificates/', include('equip_mgmt.certificates.urls')),
    path('activities/', include('equip_mgmt.m_activities.urls')),
    path('manuals/', include('equip_mgmt.manuals.urls')),
    path('spares/', include('equip_mgmt.spares.urls')),
    path('', include('equip_mgmt.common.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'equip_mgmt.core.exception_handlers.page_not_found_view'
handler500 = 'equip_mgmt.core.exception_handlers.error_view'
handler403 = 'equip_mgmt.core.exception_handlers.permission_denied_view'
handler400 = 'equip_mgmt.core.exception_handlers.bad_request_view'
