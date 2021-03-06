from django.urls import path, include
#from rest_framework import routers
from . import views 

'''
router = routers.DefaultRouter()
router.register(r'students', views.students_list)
'''
urlpatterns = [ 
    path('students/', views.students_list),
    path('students/<int:sid>/', views.student_detail),
    path('menu/', views.menu_list),
    path('menu/items/<int:low>/<int:high>/', views.menu_item_list),
    path('menu/item/<int:iid>/', views.menu_item),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

'''
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'menu', views.MenuViewSet)
router.register(r'breakfast', views.BreakfastViewSet)
router.register(r'lunch', views.LunchViewSet)
router.register(r'dinner', views.DinnerViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
'''