from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Contact
from blog.models import Post
#from django.views.generic import TemplateView
#from django.contrib.auth.mixins import LoginRequiredMixin





# Create your views here.


#class HomeView(LoginRequiredMixin, TemplateView):
    #template_name = "home.html"


def home(request):
    return render(request, "home/home.html")

def project(request):
    return render(request, "home/project.html")


def hire(request):
    return render(request, "home/hire.html")

def account(request):
    return render(request, "home/account.html")


def about(request):
    return render(request, "home/about.html")

def error(request):
    return render(request, "home/error.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        if len(name) < 2 or len(email) < 4 or len(phone) < 10 or len(content) < 3:
            messages.error(request, "Please fill the form correctly")

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, "home/contact.html")


def search(request):
    query = request.GET['query']
    # allposts = Post.objects.all()
    allposts = Post.objects.filter(title__icontains=query)
    if allposts.count()==0:
        messages.warning(request, "No search result found")

    params = {'allposts': allposts, 'query': query}
    return render(request, "home/search.html", params)
    # return HttpResponse("This is search")


def handlesingup(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #chack for error
        if len(name) < 4:
            messages.error(request, "Username must be under 4 characters")
            return redirect('home')
        #Username should only contain letters and numbers
        if not name.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')
        #Passwords do not match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        #create the user
        myuser = User.objects.create_user(name, email, pass1)
        myuser.save()
        messages.success(request, "Your ProCoder account has been successfully created")
        return redirect('home')

    else:
        return render(request, "home/error.html")


def handlelogin(request):
    #get post parameters
    if request.method == 'POST':
        loginname = request.POST['loginname']
        loginpass = request.POST['loginpass']
        user = authenticate(username= loginname, password = loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')

        else:
             messages.error(request, "Invalid Credentials, Please try again")
             return redirect('home')


    return render(request, "home/error.html")
        



def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')