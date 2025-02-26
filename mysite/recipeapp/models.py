from django.db import models
from django.contrib.auth.models import User


def get_admin_user():
    return User.objects.filter(is_superuser=True).first().pk


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Категории"

    title = models.CharField(max_length=100, verbose_name="Категория",)
    description = models.TextField(
        verbose_name="Описание категории", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category",
                               verbose_name="Автор категории")

    def description_short(self) -> str:
        if len(self.description) < 100:
            return self.description
        else:
            return self.description[:100] + "..."

    def __str__(self):
        return f"{self.title}"


def recipe_preview_directory_path(instance: "Recipe", filename:str) -> str:
                return "recipe/precipe_{pk}/preview/{filename}".format(
                    pk=instance.pk,
                    filename=filename
                )


class Recipe(models.Model):
    class Meta:
        ordering = ["title", "time_limit"]
        verbose_name_plural = "Рецепты"

    title = models.CharField(
        max_length=100, verbose_name="Рецепт", db_index=True)
    description = models.TextField(
        verbose_name="Описание рецепта", null=True, blank=True)
    step = models.TextField(
        verbose_name="Шаги приготовления", null=True, blank=True)
    time_limit = models.PositiveIntegerField(
        default=0, verbose_name="Время приготовления", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        Category, related_name="recipes", verbose_name="категории", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes",
                               verbose_name="Автор поста")
    preview_image = models.ImageField(null=True, blank=True, upload_to=recipe_preview_directory_path)
    
    def description_short(self) -> str:
        if len(self.description) < 48:
            return self.description
        else:
            return self.description[:48] + "..."
    
    def __str__(self):
        return f"Recipe(pk={self.pk}, name={self.title})"
