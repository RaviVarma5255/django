from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from siva_app.models import newone
from django.views.decorators.csrf import csrf_exempt
from siva_app.models import idea 

# Create your views here.
# indulo manamu functions rastaamu 

# def basic(request):
#     return HttpResponse("hello world!")


# def movie_review(request):
#     movie = request.GET.get('movie')
#     date = request.GET.get('date')
#     return JsonResponse({"status":"success" , "result" :{"movie_name":movie,"release_date":date}},status = 200)


# @csrf_exempt
# def cenima(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         movie = newone.objects.create(
#             movie_name = data.get("movie_name"),
#             ral_date = data.get("ral_date"),
#             budget = data.get("budget"),
#             rating = data.get("rating"),
#         )
#         return JsonResponse({
#             "status": "success",
#             "msg": "movie record inserted successfully",
#             "data": {
#                 "id": movie.id,
#                 "movie_name": movie.movie_name,
#                 "ral_date": movie.ral_date,
#                 "budget": movie.budget,
#                 "rating": movie.rating * "*",
#             }
#         }, status=200)
    
    # elif request.method == "GET":
#         ref_id = request.GET.get("id")
#         rating_id = request.GET.get("rating")
#         if  ref_id:
#             datas = newone.objects.filter(id=ref_id).values().first()
#             if datas:
#                 return JsonResponse({"status":"the single value will be appear","data":datas},status=200)
#             else:
#                 return JsonResponse({"error":"id not found"},status = 404)  
            
#         elif rating_id:
#             rating_id = int(rating_id) # convert string int 
#             datas_rating = list(newone.objects.filter(rating__gt=rating_id).values())
#             return JsonResponse({"data":datas_rating},status = 200)
#         else:
#            result_get = list(newone.objects.values())
#            print(result_get)
#            return JsonResponse({"status":"ok , the get operation will be working","data":result_get},status=200)
    

    # elif request.method == 'PUT':
    #    data1 = json.loads(request.body)
    #    ref_id1 = data1.get("id") #getting id
    #    new_movie = data1.get("movie_name") #getting movie name
    #    exisiting_movies = newone.objects.get(id=ref_id1) #fetched the object as per the id
    #    exisiting_movies.movie_name = new_movie #updating with newmovie_name
    #    exisiting_movies.save()
    #    updated_data = newone.objects.filter(id=ref_id1).values().first()
    #    print(updated_data)
    #    return JsonResponse({"status":"data updated sucsessfully","updated_data":updated_data},status = 200)
    
    # elif request.method == 'DELETE':
#         data2 = json.loads(request.body)
#         ref_id3 = data2.get("id") #getting id
#         get_dele_data = newone.objects.filter(id=ref_id3).values().first()   
#         if get_dele_data:
#             to_be_dele = newone.objects.get(id=ref_id3) 
#             to_be_dele.delete() 
#             return JsonResponse ({"status":"movie record successfully deleted","deleted data":get_dele_data},status = 200)
#         elif ref_id3 not in data2:
#             return JsonResponse ({"error":"id will not be founded"},status=404)
#     return JsonResponse({"error":"use post method"},status=400)


# def start(request):
#     a="siva"
#     b=" and i am in a learning state"
#     c= a+b
#     print(c)
#     return HttpResponse(f'my name is {c}, ok {a} good keep goin')
#like we create simple api ok next we seen render to depoly the code

# that will be done and now we use the qurey paramas

# def mov_info(request):
#     movie_name = request.GET.get("movie_name")
#     rel_date = request.GET.get("rel_date")
#     return JsonResponse({"status":"success","result":{"movie_name":movie_name,"real_date":rel_date}},status = 200)


# next vachi inko db create cheysa anudulo db name icha
# next daniki view radam

@csrf_exempt
def trying(request):

    if request.method == "POST":
        # data1 = json.loads(request.body) #if we send data through json format 
        data1 = request.POST #when we send data in form data format we have to use this
        school = idea.objects.create (nameuser = data1.get("nameuser"),
        phonenumber = data1.get("phonenumber"),
        address= data1.get("address"))
        print(school)
        return JsonResponse({"status":"success", "data":data1},status=200)
    
    elif request.method=="GET":
        #get means if ur want see all data for read and single data also if we want ..
        get = list(idea.objects.values())
        print(get)
        return JsonResponse({"status":"success","data":get})
       #1. What does idea.objects.values() return?

       # idea.objects.values() does NOT return a list.
       # It returns a QuerySet that behaves like an iterable, but it is not JSON serializable.
       # Example:
       # <QuerySet [{'id':1,'name':'Ravi'}, {'id':2,'name':'Varma'}]>
       # So Django cannot convert a QuerySet directly into JSON.

       # 2. Why do we use list() ?
       #list(idea.objects.values()) converts the QuerySet into a normal Python list.
       #Example:
       # [
       #  {'id':1,'name':'Ravi'},
       #   {'id':2,'name':'Varma'}
       # ]
       #A normal list can be converted to JSON, so JsonResponse works.
    # elif request.method == "PUT":

    
    return JsonResponse({"status":"error raised plz used post method"},status = 400)



