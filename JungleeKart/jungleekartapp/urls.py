from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                path("",views.home,name="home"),
                path("products/",views.productspage,name="products"),
                path("product/<int:id>/",views.productpage,name="product"),
                path("myAccount/",views.accountpage,name="account"),
                path("cart/",views.cartpage,name="cart"),
                path("signup/",views.signuppage,name="signup"),
                path("signin/",views.signinpage,name="signin"),
                path("logout/",views.logout_view,name="logout"),
                path("update_cart/",views.updatecartpage,name="update_cart"),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)