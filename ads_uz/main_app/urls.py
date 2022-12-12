from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("product-detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("category/<str:slug>/", views.ProductByCategoryView.as_view(), name="category_detail"),
    path("search/", views.ProductSearchView.as_view(), name="search"),
    path("add-product/", views.ProductCreateView.as_view(), name="add_product"),
    path("update-product/<int:pk>/", views.ProductUpdateView.as_view(), name="update_product"),
    path("delete-product/<int:pk>/", views.ProductDeleteView.as_view(), name="delete_product"),
    path("add-category/", views.CategoryCreateView.as_view(), name="add_category")
]
