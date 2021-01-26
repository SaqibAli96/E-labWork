from django.urls import path
from ReadBook import views 
from django.conf.urls.static import static 
from django.conf import settings 
from django.conf.urls import url
from django.views.static import serve
app_name = "ReadBook"

urlpatterns = [
    
    path('',views.loadBook, name="premiumbook"),
    path('addbook/',views.addbook, name="addbook"),
    path('description/<int:bid>/',views.bookDescription, name="description"),
    path('delete/<int:bid>/',views.deleteBook, name="deletebook"),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
