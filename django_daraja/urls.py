from django.urls import path , include
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

test_patterns = [
	# path('', views.index, name='django_daraja_index'),
	path('oauth/success', views.oauth_success, name='test_oauth_success'),
	path('stk-push/success', views.stk_push_success, name='test_stk_push_success'),
	path('business-payment/success', views.business_payment_success, name='test_business_payment_success'),
	path('salary-payment/success', views.salary_payment_success, name='test_salary_payment_success'),
	path('promotion-payment/success', views.promotion_payment_success, name='test_promotion_payment_success'),
]

urlpatterns = [
	# path('', views.index, name='index'),
	path('tests/', include(test_patterns)),
	path('', views.HeroViewSet),
	# path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

