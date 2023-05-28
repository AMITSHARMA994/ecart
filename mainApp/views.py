from django.shortcuts import render,HttpResponseRedirect
from django.db.models import Q
from .models import *
from django.contrib.auth.decorators import login_required
from random import randint
from django.conf import settings
from django.core.mail import send_mail
def homePage(Request):
    brands = Brand.objects.all()
    data = Product.objects.all().order_by("-finalprice")[0:8]
    return render(Request,"index.html",{'data':data,'brands':brands})

def shopPage(Request,mc,sc,br):
    if(mc=="All" and br=="All"):
        data = Product.objects.all().order_by("-finalprice")
    elif(mc!="All" and sc=="All" and br=="All"):
        data = Product.objects.filter(maincateory=Maincategory.objects.get(name=mc)).order_by("-finalprice")
    elif(mc=="All" and sc!="All" and br=="All"):
        data = Product.objects.filter(subcateory=subcategory.objects.get(name=sc)).order_by("-finalprice")
    elif(mc=="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(brands=brands.objects.get(name=brands)).order_by("-finalprice")
    elif(mc!="All" and sc=="All" and br=="All"):
        data = Product.objects.filter(Maincateory=maincateory.objects.get(name=mc)).order_by("-finalprice")
    elif(mc!="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(subcateory=subcateory.objects.get(name=br)).order_by("-finalprice")
    elif(mc!="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(brand=brand.objects.get(name=br)),subcateory.object.get(name=sc).order_by("-finalprice")
    else:
        data = Product.objects.filter(maincategory=maincatgaory.objects.get(name=br)).order_by("-finalprice")

    def filterPage(Request,mc,sc,br,filter):
        if(filter=="Latest"):
         if(mc=="All" and sc=="All" and br=="All"):
          data = Product.objects.all().order_by("-finalprice")
         elif(mc!="All" and sc=="All" and br=="All"):
          data = Product.objects.filter(maincateory=Maincategory.objects.get(name=mc)).order_by("-finalprice")
         elif(mc=="All" and sc!="All" and br=="All"):
          data = Product.objects.filter(subcateory=subcategory.objects.get(name=sc)).order_by("-finalprice")
         elif(mc=="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(brands=brands.objects.get(name=brands)).order_by("-finalprice")
         elif(mc!="All" and sc=="All" and br=="All"):
          data = Product.objects.filter(Maincateory=maincateory.objects.get(name=mc)).order_by("-finalprice")
         elif(mc!="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(subcateory=subcateory.objects.get(name=br)).order_by("-finalprice")
         elif(mc!="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(brand=brand.objects.get(name=br)),subcateory.object.get(name=sc).order_by("-finalprice")
         else:
          data = Product.objects.filter(maincategory=maincatgaory.objects.get(name=br)).order_by("-finalprice")
        elif(filter=="LTOH"):
            if(mc=="All"and sc=="All" and br=="All"):
              data = Product.objects.all().order_by("-finalprice")
            elif(mc!="All" and sc=="All" and br=="All"):
              data = Product.objects.filter(maincateory=Maincategory.objects.get(name=mc)).order_by("-finalprice")
            elif(mc=="All" and sc!="All" and br=="All"):
              data = Product.objects.filter(subcateory=subcategory.objects.get(name=sc)).order_by("finalprice")
            elif(mc=="All" and sc=="All" and br!="All"):
              data = Product.objects.filter(brands=brands.objects.get(name=brands)).order_by("-finalprice")
            elif(mc!="All" and sc=="All" and br=="All"):
              data = Product.objects.filter(Maincateory=maincateory.objects.get(name=mc)).order_by("-finalprice")
            elif(mc!="All" and sc=="All" and br!="All"):
              data = Product.objects.filter(subcateory=subcateory.objects.get(name=br)).order_by("-finalprice")
            elif(mc!="All" and sc=="All" and br!="All"):
              data = Product.objects.filter(brand=brand.objects.get(name=br)),subcateory.object.get(name=sc).order_by("-finalprice")
            else:
              data = Product.objects.filter(maincategory=maincatgaory.objects.get(name=br)).order_by("-finalprice")
        
    Maincategories = Maincateory.objects.all()
    Subcategories = Subcateory.objects.all()
    brands = Brand.objects.all()
    return render(Request,"shop.html",{'data':data,'maincateory':Maincateory,'subcateory':Subcateory,'brands':brands,'mc':mc,'sc':sc,'br':br})
    def priceFilterPage(Request,mc,sc,br):
        option = Request.POST.get("price")
        if(option=="1"):
          min = 0
          max = 10000 
        if(option=="2"):
          min = 0
          max = 1000
        elif(option=="3"):
          min = 1000
          max = 2000
        elif(option=="4"):
          min = 2000
          max = 3000
        elif(option=="5"):
          min = 2000
          max = 3000
        elif(option=="6"):
          min = 2000
          max = 3000
        elif(option=="7"):
          min = 5000
          max = 10000
        if(mc=="All" and br=="All"):
          data = Product.objects.filter(final_gte=min,finalprice_lte=max).order_by("-finalprice")
        elif(mc!="All" and sc=="All" and br=="All"):
          data = Product.objects.filter(maincateory=Maincategory.objects.get(name=mc),final_gte=min,finalprice_lte=max).order_by("-finalprice")
        elif(mc=="All" and sc!="All" and br=="All"):
          data = Product.objects.filter(subcateory=subcategory.objects.get(name=sc),final_gte=min,finalprice_lte=max).order_by("-finalprice")
        elif(mc=="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(brands=brands.objects.get(name=brands),final_gte=min,finalprice_lte=max).order_by("-finalprice")
        elif(mc!="All" and sc=="All" and br=="All"):
          data = Product.objects.filter(Maincateory=maincateory.objects.get(name=mc),final_gte=min,finalprice_lte=max).order_by("-finalprice")
        elif(mc!="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(subcateory=subcateory.objects.get(name=br),final_gte=min,finalprice_lte=max).order_by("-finalprice")
        elif(mc!="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(brand=brand.objects.get(name=br),final_gte=min,finalprice_lte=max),subcateory.object.get(name=sc).order_by("-finalprice")
        else:
          data = Product.objects.filter(maincategory=maincatgaory.objects.get(name=br),final_gte=min,finalprice_lte=max).order_by("-finalprice")

    def filterPage(Request,mc,sc,br,filter):
        if(filter=="Latest"):
         if(mc=="All" and sc=="All" and br=="All"):
          data = Product.objects.all().order_by("-finalprice")
         elif(mc!="All" and sc=="All" and br=="All"):
          data = Product.objects.filter(maincateory=Maincategory.objects.get(name=mc)).order_by("-finalprice")
         elif(mc=="All" and sc!="All" and br=="All"):
          data = Product.objects.filter(subcateory=subcategory.objects.get(name=sc)).order_by("-finalprice")
         elif(mc=="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(brands=brands.objects.get(name=brands)).order_by("-finalprice")
         elif(mc!="All" and sc=="All" and br=="All"):
          data = Product.objects.filter(Maincateory=maincateory.objects.get(name=mc)).order_by("-finalprice")
         elif(mc!="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(subcateory=subcateory.objects.get(name=br)).order_by("-finalprice")
         elif(mc!="All" and sc=="All" and br!="All"):
          data = Product.objects.filter(brand=brand.objects.get(name=br)),subcateory.object.get(name=sc).order_by("-finalprice")
         else:
          data = Product.objects.filter(maincategory=maincatgaory.objects.get(name=br)).order_by("-finalprice")
        elif(filter=="LTOH"):
            if(mc=="All"and sc=="All" and br=="All"):
              data = Product.objects.all().order_by("-finalprice")
            elif(mc!="All" and sc=="All" and br=="All"):
              data = Product.objects.filter(maincateory=Maincategory.objects.get(name=mc)).order_by("-finalprice")
            elif(mc=="All" and sc!="All" and br=="All"):
              data = Product.objects.filter(subcateory=subcategory.objects.get(name=sc)).order_by("finalprice")
            elif(mc=="All" and sc=="All" and br!="All"):
              data = Product.objects.filter(brands=brands.objects.get(name=brands)).order_by("-finalprice")
            elif(mc!="All" and sc=="All" and br=="All"):
              data = Product.objects.filter(Maincateory=maincateory.objects.get(name=mc)).order_by("-finalprice")
            elif(mc!="All" and sc=="All" and br!="All"):
              data = Product.objects.filter(subcateory=subcateory.objects.get(name=br)).order_by("-finalprice")
            elif(mc!="All" and sc=="All" and br!="All"):
              data = Product.objects.filter(brand=brand.objects.get(name=br)),subcateory.object.get(name=sc).order_by("-finalprice")
            else:
              data = Product.objects.filter(maincategory=maincatgaory.objects.get(name=br)).order_by("-finalprice")
        Maincategories = Maincateory.objects.all()
    Subcategories = Subcateory.objects.all()
    brands = Brand.objects.all()
    return render(Request,"shop.html",{'data':data,'maincateory':Maincateory,'subcateory':Subcateory,'brands':brands,'mc':mc,'sc':sc,'br':br})

def search(Request):
  if(Request=="POST"):
    search=Request.POST.get("search")
    data = Product.objects.filter(Q(name_contains=search)|Q(color_contains=search)|Q(size_contains=search)|Q(stock_contains=search)|Q(description_contains=search))
    Maincategories = Maincateory.objects.all()
    Subcategories = Subcateory.objects.all()
    brands = Brand.objects.all()
    return render(Request,"shop.html",{'data':data,'maincateory':Maincateory,'subcateory':Subcateory,'brands':brands,'All':mc,'All':sc,'All':br})
  else:
    return HttpResponseRedirect("/")

def singleproductPage(Request):
    return render(Request,"detail.html")

def checkoutPage(Request):
    return render(Request,"checkout.html")

def cartPage(Request):
    return render(Request,"cart.html")
@login_required(login_url="/login/")
def placeOrder(Request):
  if(Request.method=="POST"):
    buyer = Buyer.objects.get(username=Request.user.username)
    mode = Request.POST.get("mode")
    check = checkout()
    check.buyer = buyer
    subtotal = Request.session.get("subtotal",0)
    shipping = Request.session.get("shipping",0)
    total = Request.session.get("total",0)
    if(subtotal==0):
      return HttpResponseRedirect("/checkout/")


    check = Checkout()
    check.buyer = buyer()
    check.subtotal = subtotal
    check.shipping = shipping
    check.final = total
    check.save()
    

    cart = Request.session.get("cart",None)
    for key in cart.keys():
      p = Product.objects.get(id=(int(key)))
      cp = CheckoutProducts()
      cp.checkout = check
      cp.product = p
      cp.save()
    Request.session['cart'] = {}
    Request.session['subtotal'] = 0
    Request.session['shopping'] = 0
    Request.session['total'] = 0
    Request.session['count'  ] = 0
    
    subject = 'order Has Been Placed : Team E-Cart'
    message = """
              Hello"""+buyer.name+"""
              Your  Order Has Been Placed!!!
              Now Your Track Your order in Profile Section
              Team : E-Cart
              """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [buyer.email,]
    send_mail(subject,message,email_from,recipient_list)
    if(mode=="COD"):
      return HttpResponseRedirect("/confirmation/")
    else:
      orderAmount = checkout.finalAmount*100
      orderCurrency = "INR"
      paymentOrder = Client.order.create(dict(amount=orderAmount,Currency=orderCurrency,payment_capture=1))
      paymentId = paymentorder['id']
      check.paymentMode=2  
      checkout.save()
      return render(Request,"pay.html",{
        "amount":orderAmount,
        "api_key":RAZORPAY_API_KEY,
        "Order_id":paymentId,
        "user":buyer
      })

  else:
    return HttpResponseRedirect("/confirmation/")

  return HttpResponseRedirect("/checkout/")

@login_required(login_url="/login/")
def confirmation(Request):
  return render(Request,"confirmation.html")

def contactPage(Request):
  if(Request.method=="POST"):
    c = contact()
    c.name = Request.POST.get("name")
    c.email = Request.POST.get("email")
    c.phone = Request.POST.get("phone")
    c.subject = Request.POST.get("subject")
    c.message = Request.POST.get("message")
    c.save()
  return HttpResponseRedirect(Request,"contact.html")

def loginPage(Request):
  User = Request.POST.get("username")
  password = Request.POST.get("password")
  user = auth.authenticate(Username=username,password=password)
  if(user.is_superuser):
      return HttpResponseRedirect("/admin/")
  else:
      return render(Request,"profile.html")


    
  return render(Request,"login.html")

def singupPage(Request):
  return render(Request,"singup.html")
@login_required(login_url="/login/")
def profilePage(Request):
  user = User.objects.get(user=Request.user.username)
  if(user is none):
    message.error(Request,"Invaid username or Password!!!")
  else:
    auth.login(superuser,user)
    if(user.is_superuser):
      return HttpResponseRedirect("/admin/")
    else:
      buyer = Buyer.objects.get(username)
      return HttpResponseRedirect("profile",{'data':buyer})  
  return render(Request,"profile.html")

def updatePage(Request):
  return render(Request,"update.html")

def logoutPage(Request):
  auth.logout(Request)
  return HttpResponseRedirect(Request,"/logout/")

def forgetPasswordPage1(Request):
  if(Request.method=="POST"):
    username = Request.POST.get("username")
    try:
        user = Buyer.objects.get(username=username)
        otp = randiti(100000,99999999)
        user.otp
        user.save()
        subject = 'OTP for Password Reset : Team E-Cart'
        message = """
          Hello """+user.name+"""
          OTP for Password Reset is """+str(otp)+"""
          Never Share OTP with anyone
          Team : E-Cart"""

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponseRedirect("/forget-password")

    except:
        messages.error(Request,"Invalid Username ")
  return render(Request,"forget-password-1.html")


def forgetpassword2(Request):
  if(Request.method=="POST"):
    otp = Request.POST.get('otp')
    try:
       user = Buyer.objects.get(username=Request.session.get("reset-password"))
       if(otp==user.otp):
        return HttpResponseRedirect("/forget-password-3/ ")
       else:
          messages.error(Request,"Invalid OTP")
    except:
      messsage = error("UN-Authorized")
  return render(Request,"forget-password2")

def forgetpassword3(Request):
  if(Request.method=="POST"):
    password = Request.POST.get("paasword")
    cpassword = Request.POST.get("cpassword")
    if(password==cpassword):
     try:
       user = user.objects.get(username=Request.session.get("reset-password"))
       user.set_password(password)
       user,save()
       return HttpResponseRedirect("/login/")
     except:
      messsage = error(Request,"UN-Authorized")
    else:
        messages.error(Request,"passworda and Confirm Password Doesn't Matched!!!")
  return render(Request,"forget-password-3.html")