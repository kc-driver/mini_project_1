from django.conf.urls import url
from mini import views

# SET THE NAMESPACE!
app_name = 'mini'

# Be careful setting the name to just /login
# use user_login instead!

urlpatterns=[
    url(r'^register/$',views.register,name ='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]