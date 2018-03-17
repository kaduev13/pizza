from rest_framework.routers import SimpleRouter

from orders.views import OrderViewSet

router = SimpleRouter()
router.register(r'^orders', OrderViewSet, base_name='orders')

urlpatterns = router.urls
