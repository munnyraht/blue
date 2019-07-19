from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
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
    # path('contacts/', views.contactPage),
    # path('contact/', views.contact, name = 'contact'),
    # path('personaldetails/', views.Personal.as_view(), name = 'personal'),
    # path('ajax/contact', views.postContact, name ='contact_submit'),
    # url(r'home/', views.home, name='home'),
    url(r'^create$', views.create, name='create'),
    url(r'^createnextofkin$', views.createnextofkin, name='createnextofkin'),
    url(r'^createemploymentinfo$', views.createemploymentinfo, name='createemploymentinfo'),
    # url(r'^personaldetails/$', views.personaldetails, name='personaldetails'),
    url(r'^search/$', search_views.search, name='search'),
    url('loantype/', views.loantype, name='loantype'),
    url('loansummary/', views.loansummary, name='loansummary'),
    url('employmentinfo/', views.employmentinfo, name='employmentinfo'),
    url('paymentinfo/', views.paymentinfo, name='personalinfo'),
    url('acknowledgement/', views.acknowledgement, name='acknowledgement'),
    url('bvnerror/', views.bvnerror, name='bvnerror'),
    url('bvnaccepted/', views.bvnaccepted, name='bvnaccepted'),
    url('verify/', views.verifybvn, name='verifybvn'),
    url('nextofkin/', views.nextofkin, name='nextofkin'),
    url('otherdetails/', views.otherdetails, name='otherdetails'),
    url('summary/', views.summary, name='summary'),

    # Upload File 
    url(r'^terms$', views.acknowledgement_form_upload, name='acknowledgement_form_upload'),

    #Frontend Reg
    #url(r'^create_user/$',(CreateView.as_view(model=BluecreditUser, get_success_url =lambda: reverse('pending'), form_class=UserCreationForm, template_name="register")), name='register'),
    #User Dashboard
    url('creditcheck/', views.creditcheck, name='creditcheck'),
    url('loanhistory/', views.loanhistory, name='loanhistory'),
    url('repaymenthistory/', views.repaymenthistory, name='repaymenthistory'),
    url('repaymenthistory_doc/',views.repaymenthistory_doc,name='repaymenthistory_doc'),

    # Backend Urls 
    #Auth
    # path('signup/', backendviews.signup, name='signup'),
    path('register/', backendviews.signup, name='register'),
    path('pending/', backendviews.pending, name='pending'),
    # url('logout/',backendviews.login,name='logout'),
    #dashboard
    path('bluecredit/', backendviews.index, name='Home'),
    path('results/', backendviews.results, name='results'),
    path('applicant/', backendviews.personal, name='applicant'),
    path('loandetails/', backendviews.loandetails, name='loandetails'),
    path('accounts/', include('django.contrib.auth.urls'))


    # url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     core_views.activate, name='activate'),



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
