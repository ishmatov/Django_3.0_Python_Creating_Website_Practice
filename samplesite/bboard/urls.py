from django.urls import path
from .views import index, by_rubric, BbCreateView, RubricCreateView


urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('add_ad/', BbCreateView.as_view(), name='add_ad'),
    path('add_rubric/', RubricCreateView.as_view(), name='add_rubric'),
]
