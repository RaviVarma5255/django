from django.http import JsonResponse #it is used for objects like key:values 
from django.http import HttpResponse #used for "strings"

#in this we use d init and call
#and we use classes here

class MovieMiddleware:

    def __init__(self,get_rep):
        self.get_rep = get_rep

    def __call__(self, request):
        if request.path=="/movie/":
            print('movie api called')
        return self.get_rep(request )