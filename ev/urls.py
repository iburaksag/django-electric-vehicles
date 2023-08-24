from django.urls import path

from ev.views import ev_list_view, ev_details_view, ev_delete_view, ev_add_view, ev_compare_view, ev_comparison_result_view

urlpatterns = [
    path('ev_list/', ev_list_view, name='ev_list'),  
    path('ev_add/', ev_add_view, name='ev_add'),  
    path('ev_details/<int:id>/', ev_details_view, name='ev_details'),  
    path('ev_details/<int:id>/delete/', ev_delete_view, name='ev_delete'),  
    path('ev_compare/', ev_compare_view, name='ev_compare'),
    path('ev/comparison_result/', ev_comparison_result_view, name='ev_comparison_result'),
  
]

