from django.shortcuts import render

from product.models import Product,ProCot
# Create your views here.
def home(request):

    return render(request, 'home.html')

# def checkout(request):
#     return render(request, 'checkout.html')

def allProduct(request):
    data=dict()
    p =Product.objects.filter(active=True)
    data['pro'] = p

    if request.is_ajax():
        searchpro =request.GET.get('searchpro')
        cot_id =request.GET.get('cot_id',0)
        cot_id1 = int(cot_id)

        if not cot_id1 ==0:
            print(cot_id1)
            pro_obj =ProCot.objects.get(id=cot_id1)
            p3 =Product.objects.filter(cat=pro_obj)
            data['pro'] = p3

        if searchpro:
            p1 =Product.objects.filter(active=True,name__icontains=searchpro)
            data['pro'] = p1



    return render(request, 'page/allproduct.html', data)

def allCategery(request):
    pc =ProCot.objects.all()
    data ={
        'proC':pc
    }
    return render(request, 'page/allCat.html', data)





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