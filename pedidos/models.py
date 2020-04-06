from django.db import models

# Create your models here.


class Pedidos(models.Model):
    cod_cliente = models.IntegerField(blank=False, null=False)
    total_pedido = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class ItensPedido(models.Model):
    pedido  = models.ForeignKey(Pedidos,  related_name='itens_pedido', on_delete=models.CASCADE)
    produtos = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = 'Item Pedido'
        verbose_name_plural = 'Itens Pedidos'
""""
        def save(self, *args, **kwargs):
            if not self.pk:
                    self.pedido = 16
        super(ItensPedido, self).save(*args, **kwargs)
"""
