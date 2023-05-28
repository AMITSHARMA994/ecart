from django.db import models

class Maincateory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subcateory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    pic1 = models.ImageField(upload_to="brands",default=None,null=True,blank=True)
    
    def __str__(self):
        return self.name
    



class Product(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        Maincateory = models.ForeignKey(Maincateory,on_delete=models.CASCADE)
        Subcateory =models.ForeignKey(Subcateory,on_delete=models.CASCADE)
        Brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
        color = models.CharField(max_length=30)
        size = models.CharField(max_length=30)
        basesize = models.IntegerField()
        discount = models.IntegerField()
        finalprice = models.IntegerField()
        stock = models.BooleanField(default=True)
        description = models.TextField()
        pic1 = models.ImageField(upload_to="product")
        pic2 = models.ImageField(upload_to="product",default=None,null=True,blank=True)
        pic3 = models.ImageField(upload_to="product",default=None,null=True,blank=True)
        pic4 = models.ImageField(upload_to="product",default=None,null=True,blank=True)
        
        def __str__(self):
            return self.name


class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,default=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    addressline1 = models.CharField(max_length=100,default="",null=True,blank=True)
    addressline2 = models.CharField(max_length=100,default="",null=True,blank=True)
    addressline3 = models.CharField(max_length=100,default="",null=True,blank=True)
    pin = models.CharField(max_length=10,default="",null=True,blank=True)
    city = models.CharField(max_length=30,default="",null=True,blank=True)
    state = models.CharField(max_length=30,default="",null=True,blank=True)
    pic = models.ImageField(upload_to="buyers",default="",null=True,blank=True)
    otp = models.IntegerField(default=-123334)

    def __str__(self):
        return self.name+"/"+self.email  
paymentModeStatus = ((1,"COD"),( 2,"NET Banking"))
paymentStatus = ((1,"Pending"),(2,"Done"))
orderStatus = ((1,"order Place"),(2,"Ready to Dispatch"),(4,"Ready to Dispatched"),(5,"out of delivery"))
class checkout(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    paymentMode = models.IntegerField(choices=paymentModeStatus,default=1)
    paymentstatus = models.IntegerField(choices=paymentModeStatus,default=1)
    paymentorder = models.IntegerField(choices=paymentModeStatus,default=1)
    subtotal = models.IntegerField()
    shipping = models.IntegerField()
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+"/"+self.buyer.username


class checkoutProducts(models.Model):
    id = models.AutoField(primary_key=True)
    checkout = models.ForeignKey(checkout,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)+"/"+str(self.buyer.checkout.id)+" "+self.product.name
contactStatus = ((1,"Active"),(2,"Done"))
class contact(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=30)
     email = models.EmailField(max_length=50)
     phone = models.CharField(max_length=15)
     subject = models.CharField(max_length=200)
     message = models.TextField()
     status = models.IntegerField(choices=contactStatus,default=1)
     date = models.DateTimeField(auto_now=True)


     def __str__(self):
        return str(self.id)+"/"+self.name+" "+self.subject