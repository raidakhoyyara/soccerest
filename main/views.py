from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST
from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        # Hanya tampilkan produk milik user yang sedang login
        product_list = Product.objects.filter(user=request.user)
        
    context = {
        'npm' : '2406495445',
        'name': request.user.username,
        'class': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
        
    }

    return render(request, "main.html", context)

@login_required(login_url='/login/')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, "Product successfully created!")
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    # Asumsi model Product memiliki method increment_views()
    product.increment_views() 

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    product_list = Product.objects.all().order_by('-created_at') # Order by newest first
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': str(product.price) if hasattr(product, 'price') else '0.00',
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': str(product.price) if hasattr(product, 'price') else '0.00',
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
       return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # cek ajax bukan
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success', 'message': 'Account created successfully! Please log in.'})
            # Fallback untuk non-AJAX
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            # Jika form tidak valid dan ini request AJAX, kirim error sebagai JSON
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = UserCreationForm()
        
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            messages.success(request, f'Welcome back, {user.username}!')
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.info(request, 'You have been logged out.')
    return response

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Tambahkan verifikasi kepemilikan
    if product.user != request.user:
        messages.error(request, "You are not authorized to edit this product.")
        return redirect('main:show_main')
        
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request, "Product successfully updated!")
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product
    }

    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Tambahkan verifikasi kepemilikan
    if product.user != request.user:
        messages.error(request, "You are not authorized to delete this product.")
        return redirect('main:show_main')
        
    product.delete()
    messages.success(request, "Product successfully deleted!")
    return HttpResponseRedirect(reverse('main:show_main'))

def product_list(request, category=None):
    if category:
        products = Product.objects.filter(category__iexact=category)
    else:
        products = Product.objects.all()
    return render(request, "main/product_list.html", {"products": products})

@login_required(login_url='/login')
def product_by_category_view(request, category_name):
    category_slug = category_name.lower()
    filter_type = request.GET.get("filter", "all") 
    product_list = Product.objects.filter(category=category_slug) 
    
    if filter_type == "my":
        product_list = product_list.filter(user=request.user)
    
    context = {
        'category_name': category_name,
        'product_list': product_list,
        'filter_type': category_name,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

# ----------------------------------------------------------------------
# AJAX Endpoints
# ----------------------------------------------------------------------

@login_required
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    """Menambah produk baru melalui AJAX."""
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Authentication required."}, status=401)
        
    # Gunakan ProductForm untuk validasi dan sanitasi awal
    form = ProductForm(request.POST)

    if form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        # Mengembalikan JSON sukses
        return JsonResponse({"status": "created", "message": "Product successfully created!", "product_id": str(product_entry.id)}, status=201)
    else:
        # Mengembalikan pesan error validasi
        errors = dict(form.errors.items())
        # Kita hanya mengambil pesan error pertama dari setiap field
        error_messages = ", ".join([f"{k}: {v[0]}" for k, v in errors.items()])
        return JsonResponse({"status": "error", "message": f"Validation failed: {error_messages}"}, status=400)

@csrf_exempt
def create_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Product created successfully!',
                'redirect_url': reverse('main:show_main')
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required
def get_product_json(request, id):
    """Mengambil detail satu produk dalam format JSON."""
    product = get_object_or_404(Product, id=id)
    
    # Pastikan hanya pemilik produk yang bisa mengambil datanya
    if product.user != request.user:
        return JsonResponse({"status": "error", "message": "You are not authorized."}, status=403)

    data = {
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "category": product.category,
        "thumbnail": product.thumbnail,
    }
    return JsonResponse(data)

    
@login_required
@require_POST
@csrf_exempt
def edit_product_ajax(request, id):
    """Memperbarui produk melalui AJAX."""
    product = get_object_or_404(Product, id=id)

    if product.user != request.user:
        return JsonResponse({"status": "error", "message": "You are not authorized to edit this product."}, status=403)
    
    form = ProductForm(request.POST, instance=product)

    if form.is_valid():
        form.save()
        return JsonResponse({
            "status": "success", 
            "message": "Product updated successfully!",
            "redirect_url": reverse('main:show_main') 
        }, status=200)
    else:
        errors = form.errors.as_json()
        return JsonResponse({"status": "error", "message": "Validation failed", "errors": errors}, status=400)
    
@require_POST 
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        # Optional: Periksa apakah user yang request adalah pemilik produk
        if product.user != request.user:
            return JsonResponse({'status': 'error', 'message': 'You are not authorized to delete this product.'}, status=403)
            
        product.delete()
        return JsonResponse({'status': 'success', 'message': 'Product has been deleted.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)   
            

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response_data = {
                'status': 'success',
                'message': 'Login successful!',
                'redirect_url': reverse('main:show_main')
            }
            response = JsonResponse(response_data)
            response.set_cookie('last_login', str(datetime.datetime.now()), path='/')
            return response
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Account created successfully! You can now log in.'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)