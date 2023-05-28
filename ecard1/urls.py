from django.contrib import admin
from django.urls import path
from mainApp import views as mainApp
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/',admin.site.urls), 
    path('',mainApp.homePage),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shopPage),
    path('single-product/',mainApp.singleproductPage),
    path('checkout/',mainApp.checkoutPage),
    path('cart/',mainApp.cartPage),
    path('contact/',mainApp.contactPage),
    path('placeorder/',mainApp.placeOrder),
    path('confirmation/',mainApp.confirmation),
    path('login/',mainApp.loginPage),
    path('singup/',mainApp.singupPage),
    path('logout/',mainApp.logoutPage),
    path('profile/',mainApp.profilePage),
    path('forget-Password-1/',mainApp.forgetPasswordPage1),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)