from rest_framework.response import Response
from .serializers import ProductModelSerializer
from .models import PoductModel
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins, generics, status, viewsets

# Create your views here.
@api_view(['GET', 'POST'])
def ProductView(request):
    if request.method == 'POST':
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        products = PoductModel.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, pk):
    try:
        product = PoductModel.objects.get(pk=pk)
    except product.DoesNotExist:
        return Response(data={'msg':'Product not exist'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductModelSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductModelSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ProductModelSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API View Get & POST
class ProductList(APIView):
    def get(self, request):
        snippets = PoductModel.objects.all()
        serializer = ProductModelSerializer(snippets, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# API View
class CBVProductDetail(APIView):
    def get_object(self, pk):
        try:
            return PoductModel.objects.get(pk=pk)
        except PoductModel.DoesNotExist:
            raise Http404

    def get(self, pk):
        product = self.get_object(pk)
        serializer = ProductModelSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk,):
        snippet = self.get_object(pk)
        serializer = ProductModelSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response({"message": "product deleted"},status=status.HTTP_204_NO_CONTENT)

# mixins and generics
class UserGenMix(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductGenMix(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = PoductModel.objects.all()
    serializer_class = ProductModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductGenMixDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = PoductModel.objects.all()
    serializer_class = ProductModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = PoductModel.objects.all()
    serializer_class = ProductModelSerializer

#simpleviewset
class ProductSimpleViewSet(viewsets.ViewSet):
    queryset = PoductModel.objects.all()
    serializer_class = ProductModelSerializer

#genric and mixins
class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):

    queryset = PoductModel.objects.all()
    serializer_class = ProductModelSerializer


