from django.conf.urls import url
from.views import marketplace


urlpatterns = [
    url('', marketplace, name='marketplace')
]