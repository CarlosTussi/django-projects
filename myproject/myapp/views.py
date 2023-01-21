from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import InputForm, LoggerForm
# Create your views here.
def home(request):
    content ="<html><body><main><h1>My H1 tag!!</h1></main></body></html>"    

    return HttpResponse(content, content_type='text/html', charset='utf-8')

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)

def form_model_view(request):
    form = LoggerForm()
    # THIS IS THE DIFFERENCE WITH ModelForm, saving directly into the database after validated  
    if request.method == 'POST':
        form = LoggerForm(request.POST)
        if form.is_valid():
            form.save() #This will save in the database straight way
    context = {"form" : form}
    return render(request, "home.html", context)

def pathparameters(request, name, id):
    arguments = ""

    return HttpResponse("PathParameters => Name: {}, id: {}".format(name,id))


def queryparameters(request):
    name = request.GET['name']
    id = request.GET['id']

    return HttpResponse("QueryParameters => Name: {}, id:{}".format(name, id))

# Reading content from the form
def bodyparameters(request):
    if request.method == "POST":
        id=request.POST['id']
        name = request.POST['name']

    return HttpResponse("Name: {}, id:{}".format(name, id))

# NOT WORKING BECAUSE TEMPLATE NEEDS TO BE CONFIGURED FIRST
def showform(request):
 

    return render(request, 'template/form.html')

def requestcontent(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META ['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['ExtraFieldHere'] = "Some content"

    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path info: {path_info}
        <br>
        {response.headers}
        <br>
     """

    return HttpResponse(msg, content_type = 'text/html', charset='utf-8')


def error(request):
    return HttpResponseNotFound("Error raised in myapp with HttpRequestNotFound")
    


def testing(request):    
    return HttpResponse("Connecting this function directly from urls.py from project level")