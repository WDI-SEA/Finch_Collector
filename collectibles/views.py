from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TradingCardSerializer
from .models import TradingCard

# Create your views here.
class TradingCardsView(APIView):
    def get(self, request):
        cards = TradingCard.objects.all()
        data = TradingCardSerializer(cards, many=True).data
        return Response(data)
    
    def post(self, request):
        """Create TradingCard"""
        print(request.data)
        card = TradingCardSerializer(data=request.data)
        if card.is_valid():
            card.save()
            return Response(card.data, status=status.HTTP_201_CREATED)
        else:
            return Response(card.errors, status=status.HTTP_400_BAD_REQUEST)


class TradingCardDetailView(APIView):
    def get(self, request, pk):
        """Show one trading card"""
        card = get_object_or_404(TradingCard, pk=pk)
        data = TradingCardSerializer(card).data
        return Response(data)
    
    def delete(self, request, pk):
        """Deletes a card"""
        card = get_object_or_404(TradingCard, pk=pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        """Update a card"""
        # first we locate the card
        card = get_object_or_404(TradingCard, pk=pk)
        # then we run our update through the serializer
        updated_card = TradingCardSerializer(card, data=request.data)
        if updated_card.is_valid():
            updated_card.save()
            return Response(updated_card.data)
        return Response(updated_card.errors, status=status.HTTP_400_BAD_REQUEST)