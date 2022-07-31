from django.db import models
from apps.models import TimeStampedModel
# Create your models here.


class Property(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name="Predio")
    area = models.FloatField(verbose_name="Area a evaluar")
    location_code = models.CharField(max_length=50,verbose_name="Código de ubicación")

    class Meta:
        verbose_name = "Predio"
        verbose_name_plural = "Predios"

    def __str__(self):
        return self.name


class DocumentType(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name="Tipo de documento")

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipo de documentos"

    def __str__(self):
        return self.name


class Producer(TimeStampedModel):
    document_number = models.CharField(max_length=20, verbose_name="Nro. Documento")
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT, verbose_name="Tipo de docujmento")
    first_name = models.CharField(max_length=100, verbose_name="Nombres")
    last_name = models.CharField(max_length=100, verbose_name="Apellidos")

    class Meta:
        verbose_name = "Productor"
        verbose_name_plural = "Productores"

    def __str__(self):
        full_name = self.first_name + self.last_name
        return full_name


class InitialDataDetail(TimeStampedModel):
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)


class TypeSensor(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name="Tipo de sensor")

    class Meta:
        verbose_name = "Tipo de sensor"
        verbose_name_plural = "Tipo de sensores"

    def __str__(self):
        return self.name


class Sensor(TimeStampedModel):
    type_sensor = models.ForeignKey(TypeSensor, on_delete=models.PROTECT, verbose_name="Tipo de sensor")
    name = models.CharField(max_length=100, verbose_name="Nombre del sensor")

    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"

    def __str__(self):
        return self.name


class SensedDetail(TimeStampedModel):
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT)
    initial_data = models.ForeignKey(InitialDataDetail, on_delete=models.PROTECT)


class ProductType(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Tipo de producto")

    class Meta:
        verbose_name = "Tipo de producto"
        verbose_name_plural = "Tipo de productos"

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Nombre de producto")
    producto_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name="Tipo de producto")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name


class ControlType(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Tipo de control")

    class Meta:
        verbose_name = "Tipo de control"
        verbose_name_plural = "Tipos de control"

    def __str__(self):
        return self.name


class FarmControl(TimeStampedModel):
    control_type = models.ForeignKey(ControlType, on_delete=models.PROTECT, verbose_name="Tipo de control")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Producto")
    control_time = models.IntegerField(verbose_name="Tiempo de control", help_text="El tiempo de control esta basado en días")
    accumulated_production = models.IntegerField(verbose_name="Producción acumulada", help_text="La unidad de medida es en kilogramos")
    fruitful_load = models.IntegerField(verbose_name="Carga fructífera", help_text="La unidad de medida es en kilogramos")
    rain_acidity = models.IntegerField(verbose_name="Acidez de agua de lluvia")


class LandFertility(TimeStampedModel):
    ph = models.FloatField(verbose_name="PH")
    phosphorus= models.FloatField(verbose_name="Fósforo")
    nitrogen= models.FloatField(verbose_name="Nitrógeno")
    organic_material= models.FloatField(verbose_name="Materia Orgánica")
    potassium= models.FloatField(verbose_name="Potasio")
    calcium= models.FloatField(verbose_name="Calcio")
    clay= models.FloatField(verbose_name="Arcilla")
    humidity = models.FloatField(verbose_name="Humedad")
    land= models.FloatField(verbose_name="Suelo")
    land_temperature= models.FloatField(verbose_name="Temperatura del suelo")


class ShadowType(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Tipo de sombra")

    class Meta:
        verbose_name = "Tipo de sombra"
        verbose_name_plural = "Tipos de sombras"

    def __str__(self):
        return self.name


class Shadow(TimeStampedModel):
    shadow_percent = models.IntegerField(verbose_name="Porcentaje de sombra")

    class Meta:
        verbose_name = "Tipo de sombra"
        verbose_name_plural = "Tipos de sombras"

    def __str__(self):
        return self.shadow_percent


class TypeAssociatedSpecie(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Tipo de especie asociada")

    class Meta:
        verbose_name = "Tipo de especie asoaciada"
        verbose_name_plural = "Tipo de especies asociadas"

    def __str__(self):
        return self.name


class AssociatedSpecie(TimeStampedModel):
    type_associate_specie = models.ForeignKey(TypeAssociatedSpecie, on_delete=models.PROTECT, verbose_name="Tipo de especie asociada")

    class Meta:
        verbose_name = "Especie asociada"
        verbose_name_plural = "Especies asociadas"


class CoffeeType(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Tipo de café")

    class Meta:
        verbose_name = "Tipo de café"
        verbose_name_plural = "Tipos de café"

    def __str__(self):
        return self.name


class FarmProperty(TimeStampedModel):
    shadow = models.ForeignKey(Shadow, on_delete=models.PROTECT, verbose_name="Sombra")
    associated_specie = models.ForeignKey(AssociatedSpecie, on_delete=models.PROTECT, verbose_name="Especie asociada")
    coffee_type = models.ForeignKey(CoffeeType, on_delete=models.PROTECT, verbose_name="Varidad de café")
    groove_distance = models.FloatField(verbose_name="Distancia entre surcos")
    plant_age = models.FloatField(verbose_name="Edad de plantas")
    plant_distance = models.FloatField(verbose_name="Distancia entre plantas")


class FarmAbstract(TimeStampedModel):
    farm_control = models.ForeignKey(FarmControl, on_delete=models.PROTECT, verbose_name="Control de parcela")
    farm_property = models.ForeignKey(FarmProperty, on_delete=models.PROTECT, verbose_name="Propiedad de cultivo")
    land_fertility = models.ForeignKey(LandFertility, on_delete=models.PROTECT, verbose_name="Fertilidad de suelo")
    sensed = models.ForeignKey(SensedDetail, on_delete=models.PROTECT, verbose_name="Sensado")


