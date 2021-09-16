from django.db import models

# Create your models here.
class tipo_de_dulce(models.Model):
    pk_tipo_de_dulce = models.AutoField(primary_key=True, null=False, blank=False)
    sabor = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'tipo_de_dulce'
        verbose_name_plural = 'tipo_de_dulces'
        ordering = ['sabor']

    def __str__(self):
        return "{0}".format(self.sabor)


class disponible(models.Model):
    pk_disponible = models.AutoField(primary_key=True, null=False, blank=False)
    cantidad = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'disponible'
        verbose_name_plural = 'disponibles'
        ordering = ['cantidad']

    def __str__(self):
        return "{0}".format(self.cantidad)


class producto(models.Model):
    pk_producto = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    cantidad_de_venta = models.CharField(max_length=50, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)
    image = models.URLField(max_length=800, default='https://i.postimg.cc/SxTpy4DR/nodisponible.png', blank=False, null=False)
    fk_tipo_de_dulce = models.ForeignKey(tipo_de_dulce, null=False, blank=False, on_delete=models.CASCADE)
    fk_disponible = models.ForeignKey(disponible, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)


class venta(models.Model):
    pk_venta = models.AutoField(primary_key=True, null=False, blank=False)
    cantidad = models.CharField(max_length=50, null=False, blank=False)
    fk_producto = models.ForeignKey(producto, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'
        ordering = ['cantidad']

    def __str__(self):
        return "{0}".format(self.cantidad)
