from django.db import models

# Create your models here.
class Habitat(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    clima = models.CharField(max_length=60)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    

class Criatura(models.Model):
    TIPOS = [
        ('terrestre','Terrestre'),
        ('aereo', 'Aereo'),
        ('acuatico','Acuatico'),
    ]

    habitat = models.ForeignKey(
        Habitat,
        on_delete=models.PROTECT,
        related_name='criaturas',
    )
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10,choices=TIPOS)
    peligro = models.PositiveSmallIntegerField(default=1)
    tamano_cm = models.PositiveIntegerField()
    domesticable = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True)


    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
    @property
    def nivel_peligro(self):
        if self.peligro >=8:
            return "Alto"
        if self.peligro >=4:
            return "Medio"
        return "Bajo"

class Avistamiento(models.Model):
    criatura = models.ForeignKey(
        Criatura,
        on_delete=models.PROTECT,
        related_name='avistamientos',
    )
    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField(default=1)
    lugar = models.CharField(max_length=100)
    comentario = models.TextField(blank=True)
    atendido = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creada']

    def __str__(self):
        return f"{self.nombre} vio {self.criatura} el {self.fecha}"