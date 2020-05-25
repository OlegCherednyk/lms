from django.urls import path

from group.views import GroupListView, GroupUpdateViews, GroupCreateViews

app_name = 'group'

urlpatterns = [
    path('', GroupListView.as_view(), name='list'),
    path('add', GroupCreateViews.as_view(), name='add'),
    path('edit/<int:pk>', GroupUpdateViews.as_view(), name='edit'),
]