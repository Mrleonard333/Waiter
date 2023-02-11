from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .serializers import *
from .models import *

class Menu_Viewer(ListAPIView):
    serializer_class = Menu_Serializer
    queryset = Menu.objects.all()

@api_view(["POST", "PUT", "DELETE"]) # < Allowed request methods
def Menu_Edit(request):
    Data = request.data

    User_Data = Data["User_Data"]
    USER = authenticate(username=User_Data["username"], password=User_Data["password"]) # < Will check if the superuser exists

    if USER and request.method == "PUT":
        Food = Menu.objects.filter(Food=Data["Food"]).first()
        Food.Price = float(Data["Price"])
        Food.save() # < Will save the changes
        return Response({"Result":"Data modified"})

    if USER and request.method == "POST":   # v Will add the data in the DataBase fields
        New_Field = Menu_Serializer(data={"Id":Data["Id"], "Food":Data["Food"], "Price":Data["Price"]})
        New_Field.is_valid()
        New_Field.save()
        return Response({"Result":"Data saved"})

    if USER and request.method == "DELETE":
        Food = Menu.objects.filter(Food=Data["Food"]).first()
        Food.delete() # < Will delete the data
        return Response({"Result":"Data deleted"})
    
    return Response({"ERROR":"User don't have permission"}, status=401)

@api_view(["POST"])
def Make_A_Order(request):
    Data = request.data

    Order_Data = str(Data["Order"])
    Client_Name = str(Data["Client"])
    
    if Client.objects.filter(Name=Client_Name).first():
        Food_Price = Menu.objects.filter(Food=Order_Data).first()
        Food_Price = Food_Price["Price"]

                            # v Will store the DataBase data
        Id = int(len(Order.objects.all())) + 1
        Serializer = Order_Serializer(data={"Id":Id, "Name":Client_Name, "Order":Order_Data, "Price":Food_Price})

        if Serializer.is_valid():
            Serializer.save()
            return Response({"Order":Serializer.data}, status=200)
        return Response({"ERROR":"Something is missing"}, status=403)
    return Response({"ERROR":"Client is not on the list"}, status=404)

@api_view(["POST"])
def Check_Viewer(request):
    Data = request.data
    Client_Name = str(Data["Client"])

    if Client.objects.filter(Name=Client_Name).first():
        ALL = list()
        TOTAL = float()
        Orders = Order.objects.filter(Name=Client_Name)

        for O in Orders:
            TOTAL += float(O.Price)
            ALL.append({"Food":O.Order, "Price":O.Price})
        return Response({"Orders":ALL, "TOTAL":TOTAL})

    return Response({"ERROR":"Client is not on the list"}, status=404)