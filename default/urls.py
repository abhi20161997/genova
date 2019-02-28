from django.conf.urls import url

from . import views

app_name='default'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^tablets/$', views.tablets, name='tablets'),
    url(r'^injections/$', views.injections, name='injections'),
    url(r'^medicines/$', views.medicines, name='medicines'),
    url(r'^tab_product/(?P<product_id>[0-9]+)/$', views.tab_product, name='tab_product'),
    url(r'^inj_product/(?P<product_id>[0-9]+)/$', views.inj_product, name='inj_product'),
    url(r'^med_product/(?P<product_id>[0-9]+)/$', views.med_product, name='med_product'),
    url(r'^contact_response/$', views.contact_response, name='contact_response'),
    url(r'^sign_up/$', views.sign_up, name="sign_up"),
    url(r'^sign_in/$', views.sign_in, name="sign_in"),
    url(r'^buy_tablet/(?P<product_id>[0-9]+)/$', views.add_tablet_to_cart, name='add_tablet_to_cart'),
    url(r'^buy_injection/(?P<product_id>[0-9]+)/$', views.add_injection_to_cart, name='add_injection_to_cart'),
    url(r'^buy_medicine/(?P<product_id>[0-9]+)/$', views.add_medicine_to_cart, name='add_medicine_to_cart'),
    url(r'^remove_tablet/(?P<product_id>[0-9]+)/$', views.remove_tablet_from_cart, name='remove_tablet_from_cart'),
    url(r'^remove_injection/(?P<product_id>[0-9]+)/$', views.remove_injection_from_cart, name='remove_injection_from_cart'),
    url(r'^remove_medicine/(?P<product_id>[0-9]+)/$', views.remove_medicine_from_cart, name='remove_medicine_from_cart'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
    url(r'^alpha/(?P<alpha>[\w\-]+)/$', views.alpha, name='alpha'),

    # url(r'^contact_resp/$', views.contact_resp, name='contact_resp'),
]