from django.shortcuts import render
from fatora.models import Products,Orders,Customer_user
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import CartItem
from django.core.mail import send_mail
from .tasks import mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    
    if request.method == "POST":
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
        
        quantity = request.POST.get("quantity")
        if quantity:
            cart_item.quantity = int(quantity)
        cart_item.save()
        
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        context = {
            "products": product,
            "totle": total_price
        }
        return render(request, 'one_prodact.html', context=context)

    else:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        
        context = {
            "products": product,
            "totle": total_price
        }

        return render(request, 'one_prodact.html', context=context)
    
 



@login_required
def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('view_cart')


import requests
import hmac
import hashlib
import time
import json
from .rr import *

def pay(request):
    if request.method == "GET":
        return render(request, 'payment.html')
    else:
        import requests
        import hmac
        import hashlib
        import time
        import json

        def hmac_sha256(secret_key, data):
            hmac_digest = hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).digest()
            return hmac_digest

        APIKey = '0S8T25YWNJWUN6CD27QH2190kfLtXwhpbnGFdkGuHK7mmX-ms'
        sharedSecret = 'zTOhPP4N+u$$2Wtoazv2d-p$cO}Od0@MyDF1{E7F'
        URI = 'settlementv1/latest'
        QS = 'apikey=' + APIKey
        timeStampUTC = str(int(time.time()))
        payload = ''
        message = timeStampUTC + URI + QS + payload

        HMACDigest = hmac_sha256(sharedSecret, message)
        encodedDigest = HMACDigest.hex()
        XPayToken = 'xv2:' + timeStampUTC + ':' + encodedDigest
        print(XPayToken)
        headers = {
            'x-pay-token': XPayToken
        }
        payload = {
                        "msgIdentfctn": {
                            "clientId": "1VISAGCT000001",
                            "correlatnId": "12bc567d90f23e56a8f012",
                            "origId": "123451234567890"
                        },
                        "Body": {
                            "Envt": {
                                "Accptr": {
                                    "AddtlData": {
                                        "Tp": "ISOid",
                                        "Val": "42999952606"
                                    },
                                    "AddtlId": "52014057",
                                    "AddtlIds": {
                                        "Tp": "GtyMrchntData",
                                        "Val": "V070990024552"
                                    },
                                    "Adr": {
                                        "Ctry": "US",
                                        "CtrySubDvsnMjr": "48",
                                        "CtrySubDvsnMnr": "002",
                                        "PstlCd": "78641"
                                    },
                                    "CstmrSvc": "14155552235",
                                    "FrgnRtlrInd": False,
                                    "Id": "GCTstore",
                                    "PaymentFacltId": "52014057",
                                    "ShrtNm": "ABC Supplies",
                                    "SpnsrdMrchnt": {
                                        "Id": {
                                            "Id": "520140578465770"
                                        }
                                    },
                                    "Card": {
                                        "CardSeqNb": "0200",
                                        "Trck1": "B4000222357994675^CHARLES                   ^230420100558222222",
                                        "Trck2": {
                                            "HexBinryVal": "04000220130005421D230620100222222222"
                                        }
                                    },
                                    "Termnl": {
                                        "Cpblties": {
                                            "CardRdngCpblty": "MGST",
                                            "CrdhldrVrfctnCpblty": {
                                                "Cpblty": "NOOP"
                                            },
                                            "PINLngthCpblties": "05"
                                        },
                                        "TermnlId": {
                                            "Id": "VGCTapi1"
                                        }
                                    }
                                }
                            }
                        }
                    }

        url = "https://sandbox.api.visa.com/acs/v3/payments/authorizations"

        response = requests.post(
            url=url,
            headers=headers,
            json=payload
        )

                
            
                
#@login_required
#def pay2(request):
   # if request.method == "POST":
        #email = request.POST.get("email")
        #phone = request.POST.get("phone")

        
        #if len(phone) < 11:
         #   messages.error(request, 'Enter correct number')

        #else:
          
          #if email is not None and phone is not None:
            
              
            #user = Customer_user.objects.get(id=request.user.id)
            #print(user.id )
            
            #card = CartItem.objects.filter(user=request.user)
            #order_items = []
            #for item in card:
                 # Create a new Orders instance for each item
                #order_items.append(f"{item.product.name} - {item.quantity}")

                #producat=Products.objects.get(id=item.product.id)
               # print(producat)
              #  producat.count_order+=1
             #   producat.save()

            #order=Orders()
            #order.order = "\n".join(order_items) 
           # order.customer = request.user
          #  order.phone_user = phone
        ##    order.email = email
           

       #     order.save()
            # Call mail function after the loop
      #      CartItem.objects.filter(user=request.user).delete()

            
     #       mail.delay(user.id)

    #return render(request, 'payment_2.html')


