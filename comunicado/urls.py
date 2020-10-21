from django.urls import path
from . import views
# from comunicado.views import addInDiscussion, addInForum


urlpatterns = [
    path('', views.comunicado, name='comunicado'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('addInDiscussion/<int:forum_id>/', views.addInDiscussion, name='addInDiscussion'),
    # path('edit/<int:forum_id>/', views.editInForum, name='editInForum'),
    path('disc/edit/<int:discussion_id>/', views.editInDiscussion, name='editInDiscussion'),
    path('delete/<int:forum_id>/', views.deleteInForum, name='deleteInForum'),
    path('disc/delete/<int:discussion_id>/', views.deleteInDiscussion, name='deleteInDiscussion'),
]
