from django.http import HttpResponse
 
def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is the index page")
    return response

def login(request):
    response = HttpResponse()
    response.write("<h1>Login</h1>")
    response.write("This is the login page")
    return response

def register(request):
    response = HttpResponse()
    response.write("<h1>Register</h1>")
    response.write("This is the register page")
    return response
