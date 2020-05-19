from django.shortcuts import render,HttpResponse,redirect

from product.models import Product,ProCot,Cart
# Create your views here.
def home(request):

    return render(request, 'home.html')


def details_view(request,slug=None):
    p =Product.objects.get(slug=slug)
    data ={
      'pro':p
    }
    return render(request, 'page/details.html',data)

def checkout(request):
    return render(request, 'checkout.html')

def allProduct(request):
    data=dict()
    p =Product.objects.filter(active=True).order_by('-id')
    data['pro'] = p

    if request.is_ajax():
        searchpro =request.GET.get('searchpro')
        cot_id =request.GET.get('cot_id',0)
        cot_id1 = int(cot_id)

        if not cot_id1 ==0:
            print(cot_id1)
            pro_obj =ProCot.objects.get(id=cot_id1)
            p3 =Product.objects.filter(cat=pro_obj).order_by('-id')
            data['pro'] = p3

        if searchpro:
            p1 =Product.objects.filter(active=True,name__icontains=searchpro).order_by('-id')
            data['pro'] = p1



    return render(request, 'page/allproduct.html', data)

def allCategery(request):
    pc =ProCot.objects.all()
    data ={
        'proC':pc
    }
    return render(request, 'page/allCat.html', data)

def allCart(request):
    if request.is_ajax():
        pro_id = request.GET.get('pid', 0)
        pro_id =int(pro_id)
        if not pro_id==0:
            print(pro_id)
            pro_obj =Product.objects.get(id=pro_id)
            cart_match =Cart.objects.filter(product=pro_obj)
            if cart_match:
                count =int((cart_match[0].count))+1
                Cart.objects.filter(product=pro_obj).update(count=count)
            else:
                Cart.objects.create(product=pro_obj)
    pcart = Cart.objects.filter().order_by('-id')[0:5]
    pcount = Cart.objects.count()
    data = {
        'pCart': pcart,
        'pcount':pcount
    }
    return render(request, 'page/allCart.html', data)

def deleteCart(request):
    if request.is_ajax():
        pro_id = request.GET.get('pid', 0)

        pcart = Cart.objects.filter(id=pro_id)
        pcart[0].delete()
    return HttpResponse('delete')





    # if request.is_ajax():
    #     searchKey = request.GET.get('searchKey')
    #     searchKeyByid = request.GET.get('searchKeyByid',0)
    #     searchKeyByid =int(searchKeyByid)
    #
    #
    #     if searchKey:
    #         p1 = Product.objects.filter(name__startswith=searchKey)
    #         data['pro'] = p1
    #
    #     if not searchKeyByid ==0:
    #         print(type(searchKeyByid),searchKeyByid)
    #         prcOBJ = ProCot.objects.get(id=searchKeyByid)
    #         print(prcOBJ)
    #         p3=Product.objects.filter(cat=prcOBJ)
    #         data['pro'] = p3