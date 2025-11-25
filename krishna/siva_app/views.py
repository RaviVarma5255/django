from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from siva_app.models import newone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# indulo manamu functions rastaamu 

# def basic(request):
#     return HttpResponse("hello world!")


def movie_review(request):
    movie = request.GET.get('movie')
    date = request.GET.get('date')
    return JsonResponse({"status":"success" , "result" :{"movie_name":movie,"release_date":date}},status = 200)


@csrf_exempt
def cenima(request):
    if request.method == "POST":
        data = json.loads(request.body)
        movie = newone.objects.create(
            movie_name = data.get("movie_name"),
            ral_date = data.get("ral_date"),
            budget = data.get("budget"),
            rating = data.get("rating"),
        )
        return JsonResponse({
            "status": "success",
            "msg": "movie record inserted successfully",
            "data": {
                "id": movie.id,
                "movie_name": movie.movie_name,
                "ral_date": movie.ral_date,
                "budget": movie.budget,
                "rating": movie.rating * "*",
            }
        }, status=200)
    
    elif request.method == "GET":
        ref_id = request.GET.get("id")
        rating_id = request.GET.get("rating")
        if  ref_id:
            datas = newone.objects.filter(id=ref_id).values().first()
            if datas:
                return JsonResponse({"status":"the single value will be appear","data":datas},status=200)
            else:
                return JsonResponse({"error":"id not found"},status = 404)  
            
        elif rating_id:
            rating_id = int(rating_id) # convert string int 
            datas_rating = list(newone.objects.filter(rating__gt=rating_id).values())
            return JsonResponse({"data":datas_rating},status = 200)
        else:
           result_get = list(newone.objects.values())
           print(result_get)
           return JsonResponse({"status":"ok , the get operation will be working","data":result_get},status=200)
    

    elif request.method == 'PUT':
       data1 = json.loads(request.body)
       ref_id1 = data1.get("id") #getting id
       new_movie = data1.get("movie_name") #getting movie name
       exisiting_movies = newone.objects.get(id=ref_id1) #fetched the object as per the id
       exisiting_movies.movie_name = new_movie #updating with newmovie_name
       exisiting_movies.save()
       updated_data = newone.objects.filter(id=ref_id1).values().first()
       print(updated_data)
       return JsonResponse({"status":"data updated sucsessfully","updated_data":updated_data},status = 200)
    
    elif request.method == 'DELETE':
        data2 = json.loads(request.body)
        ref_id3 = data2.get("id") #getting id
        get_dele_data = newone.objects.filter(id=ref_id3).values().first()   
        if get_dele_data:
            to_be_dele = newone.objects.get(id=ref_id3) 
            to_be_dele.delete() 
            return JsonResponse ({"status":"movie record successfully deleted","deleted data":get_dele_data},status = 200)
        elif ref_id3 not in data2:
            return JsonResponse ({"error":"id will not be founded"},status=404)
    return JsonResponse({"error":"use post method"},status=400)





    
    


