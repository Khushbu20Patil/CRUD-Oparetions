from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp.models import UserModel


from rest_framework import routers
 
# import everything from views
from .views import *
 
# define the router
router = routers.DefaultRouter()
router.register('productviewset', ProductViewSet)
router.register('productmixgen', CreateListRetrieveViewSet)
router.register('productsimpleviewset', ProductSimpleViewSet)

urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),
    path('productcreate/', ProductView, name='product'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('cbv_createproduct/',ProductList.as_view()),
    path('cbv_curdproduct/<int:pk>/',CBVProductDetail.as_view()),
    path('usergenmix/',UserGenMix.as_view()),
    path('productgenmix/',ProductGenMix.as_view()),
    path('productgenmixcrud/<int:pk>',ProductGenMixDetail.as_view()),

    path('productviewset/', include(router.urls)),

    path('createlistretrieveviewset/', include(router.urls)),
    path('productsimpleviewset/', include(router.urls)),

  
]

  
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)