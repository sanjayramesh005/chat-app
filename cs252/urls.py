from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'cs252.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/', include('first.urls')),
    url(r'^api/', include('second.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
