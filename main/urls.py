from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
from main.views import product_by_category_view
from main.views import add_product_entry_ajax
from main.views import edit_product_ajax
from main.views import get_product_json
from main.views import create_product_ajax
from main.views import login_ajax, register_ajax, delete_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('product/create/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('product/edit/<str:id>/', edit_product, name='edit_product'),
    path('product/delete/<str:id>/', delete_product, name='delete_product'),
    path('category/<str:category_name>/', product_by_category_view, name='product_by_category'), 
    path('create-product-ajax', create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('get-product-json/<uuid:product_id>/', get_product_json, name='get_product_json'),
    path('login-ajax', login_ajax, name='login-ajax'),
    path('register-ajax', register_ajax, name='register-ajax'), 
    path('product/delete-ajax/<str:id>/', delete_product_ajax, name='delete_product_ajax'),   
]