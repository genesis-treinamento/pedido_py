from rest_framework import serializers

from .models import Pedidos, ItensPedido


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = ('id', 'produtos', 'pedido_id')


class PedisoSerializer(serializers.ModelSerializer):
    itens_pedido = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedidos
        fields = ('id', 'cod_cliente', 'total_pedido', 'itens_pedido')

    def create(self, validated_data):
        itens_pedido = validated_data.pop('itens_pedido')
        pedido = Pedidos.objects.create(**validated_data)
        for itens_pedido in itens_pedido:
            ItensPedido.objects.create(pedido=pedido, **itens_pedido)
        return pedido