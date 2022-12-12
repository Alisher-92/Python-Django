from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Product, Category
from .forms import CategoryForm, ProductForm
from .mixins import IsAuthenticated


def base_context():
    return {
        "categories": Category.objects.all(),
    }


class Index(ListView):
    template_name = "main_app/index.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ads.uz"
        context["header"] = "Все объявление"
        context = context | base_context()
        return context


class ProductDetailView(DetailView):
    template_name = "main_app/product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        context["header"] = self.object.title
        context = context | base_context()
        return context


class CategoryCreateView(CreateView, IsAuthenticated):
    template_name = "main_app/category_form.html"
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить рубрику"
        context["header"] = "Добавить рубрику"
        context = context | base_context()
        return context

    def form_valid(self, form):
        category = form.save(commit=False)
        messages.success(self.request, f"Рубрика: {category.name} успешно добавлен !")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("index")


class ProductCreateView(IsAuthenticated):
    @staticmethod
    def get(request):
        return render(request, template_name="main_app/product_form.html", context={
            "form": ProductForm(),
            "title": "Добавить объявление",
            "header": "Добавить объявление",
            "btn_text": "Создать",
            **base_context()
        })

    @staticmethod
    def post(request):
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            product.category.set(form.cleaned_data["category"])
            messages.success(request, f"Объявления: {product.title} успешно добавлен !")
            return redirect("index")
        else:
            messages.error(request, form.errors)
            return redirect("add_product")


class ProductUpdateView(UpdateView):
    template_name = "main_app/product_form.html"
    form_class = ProductForm

    def dispatch(self, request, *args, **kwargs):
        product = self.get_queryset().first()
        if request.user == product.author.pk:
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, "У вас нет прав для редактирования данного объявления !")
        return redirect("index")

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        product = self.object
        context = super().get_context_data(**kwargs)
        context["title"] = f"Изменить: {product.title}"
        context["header"] = f"Изменить: {product.title}"
        context["btn_text"] = "Изменить"
        context = context | base_context()
        return context

    def form_valid(self, form):
        product = form.save(commit=False)
        messages.success(self.request, f"Объявления: {product.title} успешно изменён !")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("index")


class ProductDeleteView(DeleteView):
    template_name = "main_app/product_delete.html"
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs["pk"])

    def get_success_url(self):
        product = self.object
        messages.success(self.request, f'Объявления: "{product.title}" был успешно удалён !')
        return reverse("index")


class ProductByCategoryView(Index):
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context["categories"].filter(slug=self.kwargs["slug"]).first()
        context["title"] = category.name
        context["header"] = category.name
        return context


class ProductSearchView(Index):
    def get_queryset(self):
        product_search = self.request.GET["search_product"]
        return Product.objects.filter(content__icontains=product_search)

    def get_context_data(self, **kwargs):
        product_search = self.request.GET["search_product"]
        context = super().get_context_data(**kwargs)
        context["title"] = "Поиск"
        context["header"] = f'По запросу: "{product_search}". Было найдено: {len(self.object_list)} товар(ов)'
        return context
