from django.urls import path
from ReadBook import views 
from django.conf.urls.static import static 
from django.conf import settings 

app_name = "ReadBook"

urlpatterns = [
    
    path('',views.loadBook, name="premiumbook"),
    path('addbook/',views.addbook, name="addbook"),
    path('description/<int:bid>/',views.bookDescription, name="description"),
    path('delete/<int:bid>/',views.deleteBook, name="deletebook"),



]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
