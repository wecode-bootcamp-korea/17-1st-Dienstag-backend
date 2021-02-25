import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from .models      import BagType, BagModel, Product, Color, Size, Recommendation

MODEL_ITEM_QUANTITY = 24

class CategoryListView(View):
    def get(self, request):
        bag_type_id = request.GET.get('bag_type', None)
        models      = BagType.objects.get(id=bag_type_id).bag_models.all()

        item_list = [
            {
                model.name: [
                    {
                        'id'       : product.id,
                        'image_url': product.image_url,
                    } for product in model.products.all()[:MODEL_ITEM_QUANTITY]
                ]
            } for model in models
        ]

        return JsonResponse({'data':item_list}, status=200)

class ProductListView(View):
    def get(self, request):
        bag_model_id    = request.GET.get('bag_model', None)
        keyword         = request.GET.get('keyword', None)
        products        = Product.objects.filter(Q(bag_model=bag_model_id)|Q(color__name=keyword)|Q(size__name=keyword))
        recommendations = Recommendation.objects.filter(bag_model=bag_model_id)

        model_list = [
            {
                'id'          : product.id,
                'image_url'   : product.image_url,
            } for product in products
        ]

        recommendation_list = [
            {
                'id'        : item.product.id,
                'model_name': item.product.bag_model.name,
                'image_url' : item.product.image_url,
            } for item in recommendations
        ]

        return JsonResponse({'ModelList': model_list, 'RecommendationList': recommendation_list}, status=200)

class ProductDetailView(View):
    def get(self, request):
        product_id = request.GET.get('product_id', None)
        product    = Product.objects.get(id=product_id)

        item_info = {
                'id'          : product.id,
                'image_url'   : product.image_url,
                'model_number': product.model_number,
                'price'       : product.price,
                'color_name'  : product.color.name,
                'size_name'   : product.size.name,
                'description' : product.description.split('/')
            }

        return JsonResponse({'ItemInfo': item_info}, status=200)

