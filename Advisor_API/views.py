import jwt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Advisor_API.CustomJWT import get_tokens_for_user, isAuthenticated
from Advisor_API.models import Advisor, Bookings, User
from Advisor_API.serializer import AdvisorSerializer, BookSerializer, BookingSerializer, UserSerializer
# Create your views here.

@csrf_exempt
def Add_Advisor(request):
    if request.method == 'POST':
        if len(request.body)==0:
            return JsonResponse({"message":"Body is Empty"}, status=400)
        data = JSONParser().parse(request)
        serializer = AdvisorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({"message":"Method allowed is POST not "+request.method}, status=400)

@csrf_exempt
def User_SignUp(request):
    if request.method=='POST':
        if len(request.body)==0:
            return JsonResponse({"message":"Body is Empty"}, status=400)
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            u=serializer.data["User_Id"]
            query=User.objects.filter(User_Id=u)
            res=get_tokens_for_user(query[0])
            return JsonResponse({"User_Id":u,"access-token":res}, status=200)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({"message":"Method allowed is POST not "+request.method}, status=400)


@csrf_exempt
def User_SignIn(request):
    if request.method=='POST':
        if len(request.body)==0:
            return JsonResponse({"message":" Email and Password field is required"}, status=400)
        data = JSONParser().parse(request)
        if "Email" not in data or "Password" not in data:
            return JsonResponse({"message":"Email and Password field is required"},status=400)
        query=User.objects.filter(Email=data["Email"],Password=data["Password"])
        if query:
            res=get_tokens_for_user(query[0])
            return JsonResponse({"User_Id":query[0].User_Id,'access-token':res}, status=200)
        return JsonResponse({"message":"Email or Password is incorrect"}, status=401)
    else:
        return JsonResponse({"message":"Method allowed is POST not "+request.method}, status=400)


def Get_Advisor(request,uid):
    if request.method == 'GET':
        res=isAuthenticated(request,uid)
        if res is True:
            snippets = Advisor.objects.all()
            serializer = AdvisorSerializer(snippets, many=True)
            return JsonResponse(serializer.data, safe=False)
        if res is False:
            return JsonResponse({"message":"Forbbiden"},status=403)
        if res=="Exception":
            return JsonResponse({"message":"Token Expired or Invalid Token Request new one"},status=401)
    else:
        return JsonResponse({"message":"Method allowed is GET not "+request.method}, status=400)


@csrf_exempt
def Book(request,uid,aid):
    if request.method=='POST':
        res=isAuthenticated(request,uid)
        if res is True:
            if len(request.body)==0:
                return JsonResponse({"message":"Body is Empty"}, status=400)
            data = JSONParser().parse(request)
            otherdata={"User_Id":uid,"Advisor_Id":aid}
            data=data|otherdata
            serializer = BookingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        if res is False:
            return JsonResponse({"message":"Forbbiden"},status=403)
        if res=="Exception":
            return JsonResponse({"message":"Token Expired or Invalid Token Request new one"},status=401)
    else:
        return JsonResponse({"message":"Method allowed is POST not "+request.method}, status=400)


def GetBooking(request,uid):   
    if request.method=='GET':
        res=isAuthenticated(request,uid)
        if res is True:
            data=Bookings.objects.filter(User_Id=uid).select_related('Advisor_Id')
            serializer=BookSerializer(data,many=True)
            return JsonResponse(serializer.data,safe=False,status=200)
        if res is False:
            return JsonResponse({"message":"Forbbiden"},status=403)
        if res=="Exception":
            return JsonResponse({"message":"Token Expired or Invalid Token Request new one"},status=401)
    else:
        return JsonResponse({"message":"Method allowed is GET not "+request.method}, status=400)
