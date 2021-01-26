from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from ReadBook.models import Book
from ReadBook.decorators import author_only
from django.shortcuts import Http404,HttpResponse
import os 
from django.conf import settings

def loadBook(request):
    if request.user.is_authenticated:
        books = Book.objects.all()
        return render(request,"ReadBook/Book.html",context={"books": books})
    else:
        messages.info(request,"Please login")
        return redirect("/login")
@login_required(login_url='/login/')
@author_only
def addbook(request):
    if request.user.is_authenticated:
        name = ''
        price =''
        btype = ''
        cover = ''
        pdf =  ''
        description = ''
        category = ''
        userid = ''

        if request.method == "POST":

            try:
                name = request.POST['name'].strip()
                btype = request.POST['type'].strip()
                description = request.POST['description']
                category = request.POST['category']
                cover = request.FILES.get('image',None)
                pdf = request.FILES.get('file')
                userid = request.user.id

                if btype != "Free":
                    price = int(request.POST['price'])
                else:
                    price = 0
                Book.objects.create(book_name=name,book_price=price,book_type=btype,
                book_cover=cover,book_description=description,book_category=category,book_file=pdf,uploaded_by_id=userid)

                return redirect("/")

            except Exception as e:
                print("Error:"+ str(e))

        return render(request, "ReadBook/AddBook.html",context={'bookname': name,'bookprice': price,'description': description,'category':category})
    else :
        messages.info(request,"Please login")
        return redirect("/login")


@login_required(login_url='/login/')
def bookDescription(request,bid):

    book = None
    owner = False
    loggedin = True if request.user.is_authenticated else False

    if Book.objects.filter(id=bid).exists():
        try:
            book = Book.objects.get(id=bid)
            if loggedin :
                owner = True if Book.objects.get(pk=bid).uploaded_by_id == request.user.id else False
        except Exception as e:
            print(str(e))
    else:
        return redirect("ReadBook/premiumbook")

    return render(request,"ReadBook/BookDescription.html",context={
        "book":book,
        "loggedin":loggedin,
        "owner":owner
    })
@login_required(login_url='/login/')
@author_only
def deleteBook(request,bid):
    book = None
    if Book.objects.filter(id=bid).exists():
        book = Book.objects.get(id=bid)
        book.delete()
    return redirect("/")


def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type= "application/book_file")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    
    raise Http404