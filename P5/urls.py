from django.conf.urls import patterns, include, url
#from blog.views import quick_test

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'P5.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 
#urlpatterns = patterns('',
#    url(r'^quick-test/$', quick_test),
#)




    #url(r'^admin/', include(admin.site.urls)),
    url(r'^help', 'practica5.views.help', name='help'),
    url(r'^home', 'practica5.views.home', name='home'),
    url(r'^about', 'practica5.views.about', name='about'),
)
