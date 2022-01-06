from django.urls import path
from .views.bag_views import BagsView, BagDetailView
from .views.celebrity_views import Celebrities, CelebrityDetail
from .views.product_placement_views import ProductPlacements, ProductPlacementDetail

urlpatterns = [
    path('bags/', BagsView.as_view(), name='Bags'),
    path('bags/<int:pk>/', BagDetailView.as_view(), name='Bag-detail'),
    path('celebrities', Celebrities.as_view(), name='Celebrities'),
    path('celebrities/<int:pk>/', CelebrityDetail.as_view(), name='Celebrity-detail'),
    path('product_placements/', ProductPlacements.as_view(), name='Product-Placements'),
    path('product_placements/<int:pk>/', ProductPlacementDetail.as_view())
]