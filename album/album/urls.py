"""album URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from my_clone.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainPage.as_view(), name='main-page'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^add_user/', AddUser.as_view(), name='add-user'),
    url(r'^add_photo/', AddPhoto.as_view(), name='add-photo'),
    url(r'^user_info/', UserInfo.as_view(), name='user-info'),

    url(r'^user_update/(?P<pk>(\d)+)', UpdateUser.as_view(),
        name='user-update'),

    url(r'^photo_info/(?P<photo_id>(\d)+)/$', PhotoInfo.as_view(),
        name="photo-info"),
    # url(r'^like_message/', LikeMessage.as_view(), name='like-message'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
