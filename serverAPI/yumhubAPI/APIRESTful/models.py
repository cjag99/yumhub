from django.db import models

# Create your models here.
class Author (models.Model): 
    name = models.CharField(verbose_name="Nombre",max_length=100, default="")
    last_name = models.CharField(verbose_name="Apellido",max_length=150, default="")
    email = models.EmailField(verbose_name="Email",max_length=254, default="")
    password = models.CharField(verbose_name="Contraseña",max_length=100, default="")
    created = models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición",auto_now=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["-created"]

    def __str__(self):
        return self.name + " " + self.last_name

class Category (models.Model):
    name = models.CharField(verbose_name="Nombre",max_length=100, default="")
    created = models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición",auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Ingredient (models.Model):
    VEGETAL = "VEGETAL"
    FRUTA = "FRUTA"
    CARNES = "CARNES"
    LACTEOS = "LACTEOS"
    PESCADO = "PESCADO"
    ESPECIA = "ESPECIA"
    OTROS = "OTROS"
    Ingredient_Choice = [
        (VEGETAL, "Vegetal"),
        (FRUTA, "Fruta"),
        (CARNES, "Carnes"),
        (LACTEOS, "Lacteos"),
        (PESCADO, "Pescado"),
        (ESPECIA, "Especia"),
        (OTROS, "Otros"),
    ]
    name = models.CharField(verbose_name="Nombre",max_length=100, default="")
    choice = models.CharField(verbose_name="Tipo",max_length=100, choices=Ingredient_Choice, default=OTROS)
    unit = models.CharField(verbose_name="Unidad",max_length=100, default="")
    created = models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición",auto_now=True)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Recipe (models.Model):
    name = models.CharField(verbose_name="Nombre",max_length=100, default="")
    description = models.TextField(verbose_name="Descripción", default="")
    author = models.ForeignKey(Author, verbose_name="Autor", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición",auto_now=True)

    class Meta:
        unique_together = ('name', 'author')
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class RecipeIngredient (models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name="Receta", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, verbose_name="Ingrediente", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Cantidad", default=0)
    created = models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición",auto_now=True)

    class Meta:
        unique_together = ('recipe', 'ingredient')
        verbose_name = "Ingrediente de la receta"
        verbose_name_plural = "Ingredientes de la receta"
        ordering = ["-created"]

    def __str__(self):
        return self.recipe.name + " - " + self.ingredient.name