from django.contrib import admin
from django.urls import path
from researchers import settings
from work import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('loginn/', views.loginn),
    path('signup/', views.signup),
    path('logoutt/', views.logoutt),
    path('upload', views.upload),
    path('like-post/<str:id>', views.likes, name='like-post'),
    path('#<str:id>', views.home_post),
    path('explore', views.explore),
    path('profile/<str:id_user>', views.profile),
    path('delete/<str:id>', views.delete),
    path('search-results/', views.search_results, name='search_results'),
    path('follow', views.follow, name='follow'),
    path('add-comment/<uuid:post_id>/', views.add_comment, name='add_comment'),
    path('payment/', views.payment_page, name='payment'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('payment-success/', views.payment_page, name='payment-success'),
    path('payment-cancel/', views.payment_page, name='payment-cancel'),

]
