from django.urls import path

from .views import (
    BaseView, AliasListView, AliasNewView, TargetNewView, 
    TargetListView, AliasUpdateView, AliasDeleteView,
    TargetUpdateView, TargetDeleteView)

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('<int:pk>/edit', AliasUpdateView.as_view(), name='alias_edit'),
    path('<int:pk>/edit_targ', TargetUpdateView.as_view(), name='target_edit'),
    path('alias/', AliasListView.as_view(), name='list'),
    path('new_alias/', AliasNewView.as_view(), name='new_alias'),
    path('<int:pk>/delete', AliasDeleteView.as_view(), name='alias_delete'),
    path('<int:pk>/delete_targ', TargetDeleteView.as_view(), name='target_delete'),
    path('target/', TargetListView.as_view(), name='target'),
    path('new_target/', TargetNewView.as_view(), name='new_target'),
]
