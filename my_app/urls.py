from django.urls import path, include
from . import views

# routes will be added here
urlpatterns = [
  path('blogs/<int:pk>', views.blog_detail, name='blog-detail'), # shows comments
  path('blogs/', views.index, name='index'),
  path('', views.Home.as_view(), name='home'), # connects home function from views page
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
  path('blogs/<int:pk>/edit', views.BlogUpdate.as_view(), name='blog-edit'),
  path('blogs/<int:pk>/delete', views.BlogDelete.as_view(), name='blog-delete'),
  # add CREATE blog page blogs/new
  # add EDIT blog page blogs/<int:blog_id>/edit
  # add EDIT comment page
  # add sign in sign out sign up stuff
]