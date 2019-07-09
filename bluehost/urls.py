from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.urls import path
from backend import views as backendviews
from home import views as views
from search import views as search_views

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    # url('/', views.home, name='home'),
    path('', views.home, name='home'),
    # url(r'home/', views.home, name='home'),
    url(r'^create$', views.create, name='create'),
    url(r'^createnextofkin$', views.createnextofkin, name='createnextofkin'),
    url(r'^search/$', search_views.search, name='search'),
    url('loantype/', views.loantype, name='loantype'),
    url('loansummary/', views.loansummary, name='loansummary'),
    url('employmentinfo/', views.employmentinfo, name='employmentinfo'),
    url('paymentinfo/', views.paymentinfo, name='personalinfo'),
    url('acknowledgement/', views.acknowledgement, name='acknowledgement'),
    url('declaration/', views.declaration, name='declaration'),
    url('bvnerror/', views.bvnerror, name='bvnerror'),
    url('bvnaccepted/', views.bvnaccepted, name='bvnaccepted'),
    url('verify/', views.verifybvn, name='verifybvn'),
    url('nextofkin/', views.nextofkin, name='nextofkin'),
    url('otherdetails/', views.otherdetails, name='otherdetails'),
    url('summary/', views.summary, name='summary'),
    
    # Backend Urls 
    #Auth
    path('login/', backendviews.login, name='login'),
    path('register/', backendviews.register, name='register'),
    path('pending/', backendviews.pending, name='pending'),
    #dashboard
    path('bluecredit/', backendviews.index, name='Home'),
    path('results/', backendviews.results, name='results'),
    path('applicant/', backendviews.personal, name='applicant'),
    path('loandetails/', backendviews.loandetails, name='loandetails'),
    path('salesreport/', backendviews.salesreport, name='salesreport'),




    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    # url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
