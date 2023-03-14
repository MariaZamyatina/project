
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
#from proizvodstvo.filters import AdvertisementFilter, FavouriteAdvFilter
from proizvodstvo.models import Orders
from proizvodstvo.permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyFavourites
from proizvodstvo.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    """ViewSet для заказов."""
    queryset = Orders.objects.all()
    template_name = "zakazy.html"
    serializer_class = OrderSerializer

    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(OrderViewSet, self).list(request, *args, **kwargs)
        #if request.accepted_renderer.format == 'html':
        return Response({'data': response.data}, template_name="zakazy/zakazy.html")
        #return response

    # def get_queryset(self):
    #     print(self.action)
    #     if self.action in ['retrieve', 'list']:
    #         query = Orders.objects.filter(creator_id=self.request.user.id).filter(draft=True)|\
    #                 Advertisement.objects.filter(draft=False)
    #         return query
    #     else:
    #         return Orders.objects.all()


    #filterset_class = OrdertFilter

    # @action(detail=False, methods=['get'])
    # def favourites(self, request, pk=None):
    #     """ получение списка избранных объявлений по доп. ссылке /proizvodstvo/favourites"""
    #     fav = FavouriteAdv.objects.select_related('fav_adv').filter(user_id=self.request.user.id).all()
    #     serializer = FavouriteAdvSerializer(fav, many=True)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "destroy", "partial_update"]:
            if self.request.user.is_superuser:
                return [IsAuthenticated()]
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []


# class FavouriteAdvViewSet(ModelViewSet):
#     """ избранные объявления"""
#     queryset = FavouriteAdv.objects.all()
#     filterset_class = FavouriteAdvFilter
#     serializer_class = FavouriteAdvSerializer
#     http_method_names = ["post", "patch", "delete", "head"]
#
#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)
#
#     def get_permissions(self):
#         """Получение прав для действий."""
#         if self.action in ["create", "update", "destroy", "partial_update"]:
#             if self.request.user.is_superuser:
#                 return [IsAuthenticated()]
#             return [IsAuthenticated(), IsOwnerOrReadOnlyFavourites()]
#         return []