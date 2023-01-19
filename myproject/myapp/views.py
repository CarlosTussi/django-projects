from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    content ="<html><body><main><h1>My H1 tag!!</h1></main></body></html>"
    path = request.path + "extra!dasdasds"

    return HttpResponse(path, content_type='text/html', charset='utf-8')
    

def testing(request):
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