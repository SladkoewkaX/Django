from django.urls import path


from .views import cars_list, car_detail, main


app_name='test_app'

# urlpatterns = [
#     path('index/', index),
#
urlpatterns = [
    path('', main),
    path('cars/', cars_list, name = 'cars'),
    path('<int:pk>', car_detail, name= 'car')
   
]
