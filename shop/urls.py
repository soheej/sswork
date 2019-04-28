from django.urls import path, register_converter
from shop import views
from shop import converters

app_name = 'shop'

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('view/<int:pk>/', views.item_detail, name='item_detail'),
    path('new/', views.item_new, name='item_new'),
    path('remove/<int:pk>/', views.item_remove, name='item_remove'),
    path('edit/<int:pk>/', views.item_edit, name='item_edit'),
    path('excel/', views.response_excel),
    path('image/', views.response_image),
    path('mysum/<int:x>/<int:y>/', views.my_sum),
    path('archives/<yyyy:year>/', views.year_archive),
    path('test_templates/', views.test_templates),  # 추가
]