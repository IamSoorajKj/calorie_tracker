from django.shortcuts import render,get_object_or_404

from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from calorie_management.serializers import FoodLogSerializer
from calorie_management.models import FoodLog
from calorie_management.permissions import IsOwner


from datetime import datetime

# Create your views here.

class CalorieListCreateView(APIView):

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[permissions.IsAuthenticated]

  def get(self,request):

    auth_user=request.user

    qs=FoodLog.objects.filter(owner=auth_user)

    serializer_instance=FoodLogSerializer(qs,many=True)

    return Response(serializer_instance.data)
  
  def post(self,request):

    form_data=request.data

    serializer_instance=FoodLogSerializer(data=form_data)

    if serializer_instance.is_valid():

      serializer_instance.save(owner=request.user)

      return Response(serializer_instance.data)

    else:
      
      return Response(serializer_instance.errors)


class CalorieRetrieveUpdateDeleteView(APIView):

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[IsOwner]

  def get(self,request,pk=None):

    qs=get_object_or_404(FoodLog,id=pk)

    self.check_object_permissions(request,qs)

    serializer_instance=FoodLogSerializer(qs)

    return Response(serializer_instance.data)
  
  def put(self,request,pk=None):

    instance=get_object_or_404(FoodLog,id=pk)

    self.check_object_permissions(request,instance)

    form_data=request.data

    serializer_instance=FoodLogSerializer(data=form_data,instance=instance)

    if serializer_instance.is_valid():

      serializer_instance.save()

      return Response(serializer_instance.data)

    else:

      return Response(serializer_instance.errors)
    

  def delete(self,request,pk=None):


    qs=get_object_or_404(FoodLog,id=pk)

    self.check_object_permissions(request,qs)

    qs.delete()

    return Response({"message":"calorie deleted...."})


class CalorieSummaryView(APIView):

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[permissions.IsAuthenticated]


  def get(self,request):

    auth_user_calories=FoodLog.objects.filter(owner=request.user)

    curr_date=datetime.today().date()

    response_data={
      "todays_total_calorie":0,
      "monthly_calorie":0
    }

    #todays_total_calorie

    todays_total_calorie=auth_user_calories.filter(created_at__date=curr_date).values("calorie").aggregate(total=Sum("calorie")).get("total")

    #monthly_calorie


    curr_month=datetime.today().month

    curr_year=datetime.today().year

    monthly_calorie=auth_user_calories.filter(created_at__month=curr_month,created_at__year=curr_year).values("calorie").aggregate(total=Sum("calorie")).get("total")
    
    #assigning both month,today calorie
    
    response_data["todays_total_calorie"]=todays_total_calorie

    response_data["monthly_calorie"]=monthly_calorie

    return Response(response_data)







