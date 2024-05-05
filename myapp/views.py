from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout,get_user_model
from myapp.models import User_work,UserProfile,Product,Cart,Order,OrderStatus,Cart_list,Values
from django.core import mail
from django.conf import settings
import random


from django.db.models.signals import post_save
from django.dispatch import receiver


global no
global captcha

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product':product})

def create_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('f1')
        last_name = request.POST.get('l1')
        email = request.POST.get('e1')
        user = request.POST.get('u1')
        pwd = request.POST.get('p1')

        if User.objects.filter(username=user).exists():
            msg = 'User is already exists try different username'
            return render(request,'regs.html',{'msg':msg})
        else:
            User.objects.create_user(username=user, password=pwd,email=email,first_name=first_name,last_name=last_name)

            msg = 'User is registered successfully'
            return render(request,'regs.html',{'msg':msg})

def admin_login(request):
    global captcha
    if request.method == 'POST':
        user = request.POST.get('p1')
        pwd = request.POST.get('p2')
        cap = request.POST.get('p3')
        if int(cap) == int(captcha):

            u = authenticate(request,username=user,password=pwd)
            if u is not None:
                login(request,u)

                return render(request, 'dash.html')
            else:
                error = 'Invalid Username or password'
                return render(request, 'login_user.html', {'msg1': error})
        else:

            captcha = random.randint(10000, 999999)
            error = 'Captcha not match. Try again.'
            return render(request,'login_user.html',{'msg1':error,'cap':captcha})





def normal_user(request):
    if request.method == 'POST':
        user = request.POST.get('t1')
        pwd = request.POST.get('t2')
        if User_work.objects.filter(username=user).exists():
            error = 'User already exists try different name'
            return render(request,'index.html',{'msg':error})
        else:
            data = User_work.objects.create(username=user,password=pwd)
            data.save()
            msg = 'User register successfully'
            return render(request,'index.html',{'msg':msg})

def normal_login(request):
    if request.method == 'POST':
        user = request.POST.get('p1')
        pwd = request.POST.get('p2')
        try:
            user = User_work.objects.get(username=user,password=pwd)
            return redirect('dash')
        except User_work.DoesNotExist:
            error = 'Invalid Username or password'
            return render(request,'login_user.html',{'msg1':error})

def dash(request):
    return render(request,'dash.html')

def normal_logout(request):
    return render(request,'index.html')


def login_user(request):
    global captcha
    captcha = random.randint(10000,999999)
    return render(request,'login_user.html',{'cap':captcha})

def logout_user(request):

    logout(request)
    global captcha
    captcha = random.randint(10000, 999999)
    return render(request,'login_user.html',{'cap':captcha})

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

def regs(request):
    return render(request,'regs.html')

def example(request):

    return render(request, 'example.html')


def profile(request):
    user = request.user
    add = UserProfile.objects.filter(user=user)
    return render(request,'profile.html',{'user':user,'add':add})


def add_address(request):
    return render(request,'add_address.html')

def save_address(request):
    if request.method == 'POST':
        user = request.user
        address = request.POST.get('add')
        pin = request.POST.get('pin')
        phone = request.POST.get('phone')

        data = UserProfile.objects.create(user=user,address=address,pin=pin,phone=phone)
        data.save()

        msg = 'Address is added in the account'
        return render(request,'dash.html',{'msg_address':msg})


def add_to_cart(request,id):
    data = Product.objects.filter(id=id)
    user = request.user

    for i in data:
        title = i.item
        img = i.photo
        price = i.price


    Cart.objects.create(product_item=title,img=img,price=price,user=user)
    msg = 'Product added in the Cart'
    product = Product.objects.all()
    return render(request,'index.html',{'product':product})

def clear_cart(request):
    data = Cart.objects.filter(user=request.user)
    data.delete()
    data1 = Cart_list.objects.filter(user=request.user)
    data1.delete()
    return render(request,'cart.html')


def cart(request):
    product = Cart.objects.filter(user=request.user)
    atoast = []
    stoast = []
    sptoast = []
    mtoast = []
    cdonuts = []
    rdonuts = []
    mbread = []
    zbread = []

    aimg = ''
    simg = ''
    spimg = ''
    mimg = ''
    cimg = ''
    rimg = ''
    mbimg = ''
    zimg = ''

    for i in product:
        if i.product_item == 'Ashu Toast':
            aimg = i.img
            atoast.append(i.product_item)
        elif i.product_item == 'Shaktiman Toast':
            simg = i.img
            stoast.append(i.product_item)
        elif i.product_item == 'Special Toast':
            spimg = i.img
            sptoast.append(i.product_item)
        elif i.product_item == 'MilkToast':
            mimg = i.img
            mtoast.append(i.product_item)
        elif i.product_item == 'Cream Donuts':
            cimg = i.img
            cdonuts.append(i.product_item)
        elif i.product_item == 'Round Donuts':
            rimg = i.img
            rdonuts.append(i.product_item)
        elif i.product_item == 'Milk Bread':
            mbimg = i.img
            mbread.append(i.product_item)
        elif i.product_item == 'Zoya Bread':
            zimg = i.img
            zbread.append(i.product_item)
        else:
            pass

    if len(atoast) >= 1:
        item = "Ashu Toast"
        quantity = len(atoast)
        price = len(atoast) * 20
        img = aimg
        if len(atoast) >= 1:
            Cart_list.objects.filter(item=item).delete()
        Cart_list.objects.create(item=item, quantity=quantity, amount=price, user=request.user, img=img)

    if len(stoast) >= 1:
        item = "Shaktiman Toast"
        quantity = len(stoast)
        price = len(stoast) * 10
        img = simg
        if len(stoast) >= 1:
            Cart_list.objects.filter(item=item).delete()
        Cart_list.objects.create(item=item, quantity=quantity, amount=price, user=request.user, img=img)

    if len(sptoast) >= 1:
        item = "Special Toast"
        quantity = len(sptoast)
        price = len(sptoast) * 50
        img = spimg
        if len(sptoast) >= 1:
            Cart_list.objects.filter(item=item).delete()
        Cart_list.objects.create(item=item, quantity=quantity, amount=price, user=request.user, img=img)

    if len(mtoast) >= 1:
        item = "MilkToast"
        quantity = len(mtoast)
        price = len(mtoast) * 30
        img = mimg
        if len(mtoast) >= 1:
            Cart_list.objects.filter(item=item).delete()
        Cart_list.objects.create(item=item, quantity=quantity, amount=price, user=request.user, img=img)

    if len(cdonuts) >= 1:
        item = "Cream Donuts"
        quantity = len(cdonuts)
        price = len(cdonuts) * 100
        img = cimg
        if len(cdonuts) >= 1:
            Cart_list.objects.filter(item=item).delete()
        Cart_list.objects.create(item=item, quantity=quantity, amount=price, user=request.user, img=img)

    if len(rdonuts) >= 1:
        item = "Round Donuts"
        quantity = len(rdonuts)
        price = len(rdonuts) * 50
        img = rimg
        if len(rdonuts) >= 1:
            Cart_list.objects.filter(item=item).delete()
        Cart_list.objects.create(item=item, quantity=quantity, amount=price, user=request.user, img=img)

    if len(mbread) >= 1:
        item = "Milk Bread"
        quantity = len(mbread)
        price = len(mbread) * 20
        img = mbimg
        if len(mbread) >= 1:
            Cart_list.objects.filter(item=item).delete()
        Cart_list.objects.create(item=item, quantity=quantity, amount=price, user=request.user, img=img)

    if len(zbread) >= 1:
        item = "Zoya Bread"
        quantity = len(zbread)
        price = len(zbread) * 50
        img = zimg
        if len(mbread) >= 1:
            Cart_list.objects.filter(item=item).delete()
        Cart_list.objects.create(item=item, quantity=quantity, amount=price, user=request.user, img=img)

    cart = Cart_list.objects.filter(user=request.user)

    return render(request, 'cart.html', {'cart': cart})



def checkout(request):
    product = Cart_list.objects.filter(user=request.user)
    number = Cart.objects.filter(user=request.user)
    value = []
    for i in number:
        j = i.price
        value.append(j)
    total = sum(value)
    gst = total * 18 / 100
    courier = 30
    gtotal = gst + courier + total

    add = UserProfile.objects.filter(user=request.user)
    return render(request, 'checkout.html', {'cart': product,'add':add,'total':total,'gst':gst,'courier':courier,'gtotal':gtotal})



def order(request):
    ord = Order.objects.filter(user=request.user)
    return render(request, 'example.html', {'product': ord})




def tvalue(request,gtotal):
    value = gtotal
    return render(request,'payment.html',{'value':value})

def payment(request):
    ord = Order.objects.filter(user=request.user)
    total_list = []
    return render(request,'payment.html')



def order_new(request):

    cart = Cart_list.objects.filter(user=request.user)

    number = Cart.objects.filter(user=request.user)
    value = []
    for i in number:
        j = i.price
        value.append(j)
    total = sum(value)
    gst = total * 18 / 100
    courier = 30
    gtotal = gst + courier + total

    order = Order.objects.create(user=request.user, price=gtotal)
    for carts in cart:
        title = carts.item
        quantity = carts.quantity
        order.item.create(value=title, quantity=quantity, user=request.user)

    ca = Cart.objects.filter(user=request.user)
    ca.delete()
    da = Cart_list.objects.filter(user=request.user)
    da.delete()

    ord = Order.objects.filter(user=request.user)

    return render(request, 'order.html', {'product': ord})


def order_status(request,id):
    product = Order.objects.get(no=id)
    abc = product.order_status

    value = str(abc)
    if value == 'Shipped':
        value_size = 10
        bg = 'bg-danger'
    elif value == 'Transmission':
        value_size = 25
        bg = 'bg-warning'
    elif value == 'On the way':
        value_size = 50
        bg = 'bg-primary'

    elif value == 'Out for delivery':
        value_size = 75
        bg = 'bg-info'
    elif value == 'Delivered':
        value_size = 100
        bg = 'bg-success'
    else:
        value_size = 0
        bg = 'bg-warning'

    return render(request, 'order_status.html',{'product':product,'value_size':value_size,'bg':bg,'value':value})



def contact(request):
    return render(request,'contact.html')



def sendmail(request):
    global no
    no = random.randint(1000, 9999)
    connection = mail.get_connection()
    connection.open()
    subject = 'OTP Verification'
    message = str(no)
    email1 = request.POST.get('t1')
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email1]
    email = mail.EmailMessage(subject,message,from_email,recipient_list)
    connection.send_messages([email])
    connection.close()
    output = "OTP sent successfully"
    return render(request, 'otp.html',{'msg':output,'email':email1})

def check(request):
    global no
    if request.method == 'POST':
        email = request.POST.get('email')
        no_receive = request.POST.get('n1')
        if int(no_receive) == int(no):
            msg = "OTP is match"
            return render(request,'regs.html',{'email':email})
        else:
            msg = "OTP is not match try again"
            return render(request,'otp.html',{'msg':msg,'email':email})


def email(request):

    return render(request,'email.html')






































