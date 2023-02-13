# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_daraja.mpesa import utils
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from rest_framework import status
from .serializers import HroSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view,action
from .models import Hro
cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

# stk_push_callback_url = 'https://www.kopaloanswin.xyz/'
# b2c_callback_url = 'https://darajambili.herokuapp.com/b2c/result'
message = 'Kindly Input M-pesa PIN when promted.'

global friends_no
price = 0
response = "CON Main menu\n"
fm = ''
text  = None
global phone_number
@csrf_exempt
@api_view(['GET', 'POST'])
def HeroViewSet(request):
    if request.method == 'GET':
        heros = Hro.objects.all()
        serializer = HroSerializer(heros,many=True)
        return JsonResponse(serializer.data, safe=False)
        # p=len(queryset)
        # l = p-1
        # print(queryset[l])


    elif request.method == 'POST':
        global price
        global response
        global text
        empty = "CON Please Input parameters"
        texty = {"input":'Maybe empty but must have parameter'}
        serializer = data=request.data
        # serialize = HroSerializer(data=request.data)
        print(serializer)
        if serializer:
            
            phone_number = serializer.get("msisdn")
            session_id = serializer.get("sessionID")
            service_code = serializer.get("accessPoint")
            text = serializer.get("input")
            print(phone_number)
            # print(text)



            if text is None and phone_number:
             
                response = "CON Main menu\n"
                response += "1. Buy Data Deals\n"
                response += "2. Gift Data Bundles\n"
                response += "3. Buy Airtime ansd Get 100% Bonus\n"

            if text == '':
             
                response = "CON Main menu\n"
                response += "1. Buy Data Deals\n"
                response += "2. Gift Data Bundles\n"
                response += "3. Buy Airtime ansd Get 100% Bonus\n"


            elif text == '1':
                print(text)
                response = "CON Buy Data Deals \n"
                response += "1. Sh49=2GB  for 30days \n"
                response += "2. Sh99=5GB for 30days  \n"
                response += "3. Sh199=10GB for 30days \n"
                response += "4. Sh499=25GB for 30days \n"

            elif text:
                array = text.split('*')
                # print(len(array))
                if (len(array) == 2 and int(array[0]) == 1):
                    if (int(array[1]) == 1):

                        response = "CON Confirm Purchase of Sh49=2GB for 30days \n"
                        response += "1. Auto-Renew \n"
                        response += "2. Buy Once \n"
                    elif (int(array[1]) == 2):
                        response = "CON Confirm Purchase of Sh99=5GB for 30days \n"
                        response += "1. Auto-Renew \n"
                        response += "2. Buy Once \n"

                    elif (int(array[1]) == 3):
                        response = "CON Confirm Purchase of Sh249=10GB for 30days \n"
                        response += "1. Auto-Renew \n"
                        response += "2. Buy Once \n"

                    elif (int(array[1]) == 4):
                        response = "CON Confirm Purchase of Sh499=25GB for 30days \n"
                        response += "1. Auto-Renew \n"
                        response += "2. Buy Once \n"

                elif (len(array) == 3 and int(array[0]) == 1):
                    if (int(array[1]) == 1):
                        if (int(array[2]) == 1):
                            price = 49
                            response = f"END You have purchased 2GB GB Data {message} \n", stk_push_success(
                                request)
                        elif (int(array[2]) == 2):
                            price = 49
                            response = f"END You have purchased 2GB GB Data {message} \n", stk_push_success(
                                request)

                    elif (int(array[1]) == 2):
                        if (int(array[2]) == 1):
                            price = 99
                            response = f"END You have purchased 5GB GB Data {message} \n", stk_push_success(
                                request)
                        elif (int(array[2]) == 2):
                            price = 99
                            response = f"END You have purchased 5GB GB Data {message} \n", stk_push_success(
                                request)

                    elif (int(array[1]) == 3):
                        if (int(array[2]) == 1):
                            price = 199
                            response = f"END You have purchased 10GB GB Data {message} \n", stk_push_success(
                                request)
                        elif (int(array[2]) == 2):
                            price = 199
                            response = f"END You have purchased 10GB GB Data {message} \n", stk_push_success(
                                request)
                        elif (int(array[2]) == 2):
                            price = 199
                            response = f"END You have purchased 10GB GB Data {message} \n", stk_push_success(
                                request)

                    elif (int(array[1]) == 4):
                        if (int(array[2]) == 1):
                            price = 499
                            response = f"END You have purchased 25GB GB Data {message} \n", stk_push_success(
                                request)
                        elif (int(array[2]) == 2):
                            price = 499
                            response = f"END You have purchased 25GB GB Data {message} \n", stk_push_success(
                                request)


    # --------------------------------------second tier sambaza airtime-----------------------------------------

                elif (len(array) == 1 and int(array[0]) == 3):

                    print(array[0])
                    if (len(array) == 1):
                        response = "CON Buy Airtime Deals \n"
                        response += "1. Sh50=100  bob airtime \n"
                        response += "2. Sh100=200 bob artime  \n"
                        response += "3. Sh200=500 bob artime \n"
                        response += "4. Sh500=2000 artime \n"

                elif (len(array) == 2 and int(array[0]) == 3):
                    if (int(array[1]) == 1):
                        response = f"CON Confirm Purchase of Sh50=100 bob airtime \n"
                        response += "1. Auto-Renew \n"
                        response += "2. Buy Once \n"

                    elif (int(array[1]) == 2):
                        response = f"CON Confirm Purchase of Sh100=200 bob airtime \n"
                        response += "1. Auto-Renew \n"
                        response += "2. Buy Once \n"
                    elif (int(array[1]) == 3):
                        response = f"CON Confirm Purchase of Sh200=500 bob airtime \n"
                        response += "1. Auto-Renew \n"
                        response += "2. Buy Once \n"
                    elif (int(array[1]) == 4):
                        response = f"CON Confirm Purchase of Sh500=2000 bob airtime \n"
                        response += "1. Auto-Renew \n"
                        response += "2. Buy Once \n"
                elif (len(array) == 3 and int(array[0]) == 3):
                    if (int(array[2]) == 1 and int(array[1]) == 1):
                        price = 50
                        response = f"END You have purchased sh100 airtime {message} \n", stk_push_success(
                            request)
                    elif (int(array[2]) == 2 and int(array[1]) == 1):
                        price = 50
                        response = f"END You have purchased sh100 airtime {message} \n", stk_push_success(
                            request)

                    elif (int(array[2]) == 1 and int(array[1]) == 2):
                        price = 50
                        response = f"END You have purchased sh200 airtime {message} \n", stk_push_success(
                            request)
                    elif (int(array[2]) == 2 and int(array[1]) == 2):
                        price = 50
                        response = f"END You have purchased sh200 airtime {message} \n", stk_push_success(
                            request)
                    elif (int(array[2]) == 2 and int(array[1]) == 2):
                        price = 50
                        response = f"END You have purchased sh200 airtime {message} \n", stk_push_success(
                            request)

                    elif (int(array[2]) == 1 and int(array[1]) == 3):
                        price = 200
                        response = f"END You have purchased sh500 airtime {message} \n", stk_push_success(
                            request)
                    elif (int(array[2]) == 2 and int(array[1]) == 3):
                        price = 200
                        response = f"END You have purchased sh500 airtime {message} \n", stk_push_success(
                            request)

                    elif (int(array[2]) == 1 and int(array[1]) == 4):
                        price = 500
                        response = f"END You have purchased sh2000 airtime {message} \n", stk_push_success(
                            request)
                    elif (int(array[2]) == 2 and int(array[1]) == 4):
                        price = 500
                        response = f"END You have purchased sh2000 airtime {message} \n", stk_push_success(
                            request)

                elif (len(array) == 1):
                    if (int(array[0]) == 2):

                        response = 'CON Please Enter Phone Number'

                elif text:

                    if (len(array) == 2 and int(array[0]) == 2):
                        response = "CON Buy Data Deals For a friend\n"
                        response += "1. Sh49=2GB  for 30days \n"
                        response += "2. Sh99=5GB for 30days  \n"
                        response += "3. Sh199=10GB for 30days \n"
                        response += "4. Sh499=25GB for 30days \n"

                    elif (len(array) == 3):
                        friends_no = array[1]
                        if (int(array[2]) == 1):

                            response = f"CON Confirm Purchase of Sh49=2GB for for {friends_no} valid for 30days \n"
                            response += "1. Auto-Renew \n"
                            response += "2. Buy Once \n"
                        elif (int(array[2]) == 2):
                            response = f"CON Confirm Purchase of Sh99=5GB for for {friends_no} valid for 30days \n"
                            response += "1. Auto-Renew \n"
                            response += "2. Buy Once \n"

                        elif (int(array[2]) == 3):
                            response = f"CON Confirm Purchase of Sh199=10GB for for {friends_no} valid for 30days \n"
                            response += "1. Auto-Renew \n"
                            response += "2. Buy Once \n"

                        elif (int(array[2]) == 4):
                            response = f"CON Confirm Purchase of Sh499=25GB for for {friends_no} valid for 30days \n"
                            response += "1. Auto-Renew \n"
                            response += "2. Buy Once \n"

                    elif (len(array) == 4):
                        if (int(array[2]) == 1):
                            if (int(array[3]) == 1):
                                price = 49
                                response = f"END You have purchased 2GB GB Data {message} \n", stk_push_success(
                                    request)
                            elif (int(array[3]) == 2):
                                price = 49
                                response = f"END You have purchased 2GB GB Data {message} \n", stk_push_success(
                                    request)

                        elif (int(array[2]) == 2):
                            if (int(array[3]) == 1):
                                price = 99
                                response = f"END You have purchased 5GB GB Data {message} \n", stk_push_success(
                                    request)
                            elif (int(array[3]) == 2):
                                price = 99
                                response = f"END You have purchased 5GB GB Data {message} \n", stk_push_success(
                                    request)

                        elif (int(array[2]) == 3):
                            if (int(array[3]) == 1):
                                price = 199
                                response = f"END You have purchased 10GB GB Data {message} \n", stk_push_success(
                                    request)
                            elif (int(array[3]) == 2):
                                price = 199
                                response = f"END You have purchased 10GB GB Data {message} \n", stk_push_success(
                                    request)

                        elif (int(array[2]) == 4):
                            if (int(array[3]) == 1):
                                price = 499
                                response = f"END You have purchased 25GB GB Data {message} \n", stk_push_success(
                                    request)
                            elif (int(array[3]) == 2):
                                price = 499
                                response = f"END You have purchased 25GB GB Data {message} \n", stk_push_success(
                                    request)
                            elif (int(array[3]) == 2):
                                price = 499
                                response = f"END You have purchased 25GB GB Data {message} \n", stk_push_success(
                                    request)


    # ---------------------------tier 3----------------------------------------------------
            # return Response(response, status=status.HTTP_201_CREATED)
        # else:
                # return Response(texty, status=status.HTTP_400_BAD_REQUEST)
                print(text)
            return HttpResponse(response,status=status.HTTP_201_CREATED)
        else:
            return Response(empty, status=status.HTTP_400_BAD_REQUEST)
        




def oauth_success(request):
        r = cl.access_token()
        return JsonResponse(r, safe=False)

def stk_push_success(request):
    global phone_number
    print(phone_number)

    phone_number=request.POST.get('msisdn')

    global price
    global fm
    print(price)
    phone_number = phone_number
    amount = price
    account_reference = 'Glownet Solutions'
    transaction_desc = 'STK Push Description'
    callback_url = stk_push_callback_url
    r = cl.stk_push(phone_number, amount, account_reference,
                    transaction_desc, callback_url)
    # customer = {"phone_number":'phone_number'}
    return JsonResponse(r.response_description, safe=False)
    # return Response(customer, status=status.HTTP_200_OK)


def business_payment_success(request):
    phone_number = config('B2C_PHONE_NUMBER')
    amount = 1
    transaction_desc = 'Business Payment Description'
    occassion = 'Test business payment occassion'
    callback_url = b2c_callback_url
    r = cl.business_payment(phone_number, amount,
                            transaction_desc, callback_url, occassion)
    return JsonResponse(r.response_description, safe=False)


def salary_payment_success(request):
    phone_number = config('B2C_PHONE_NUMBER')
    amount = 1
    transaction_desc = 'Salary Payment Description'
    occassion = 'Test salary payment occassion'
    callback_url = b2c_callback_url
    r = cl.salary_payment(phone_number, amount,
                          transaction_desc, callback_url, occassion)
    return JsonResponse(r.response_description, safe=False)


def promotion_payment_success(request):
    phone_number = config('B2C_PHONE_NUMBER')
    amount = 1
    transaction_desc = 'Promotion Payment Description'
    occassion = 'Test promotion payment occassion'
    callback_url = b2c_callback_url
    r = cl.promotion_payment(phone_number, amount,
                             transaction_desc, callback_url, occassion)
    return JsonResponse(r.response_description, safe=False)

