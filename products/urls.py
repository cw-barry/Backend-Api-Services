from rest_framework import routers
from .views import CategoryView, ProductView

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('', ProductView)

urlpatterns = [

]

urlpatterns += router.urls