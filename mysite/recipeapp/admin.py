from django.contrib import admin
from recipeapp.models import Recipe, Category


class CategoryInLine(admin.TabularInline):
    model = Recipe.categories.through 
    verbose_name_plural = "Добавить категории"


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "description", "step", "time_limit", "created_at",
    ordering = "pk", "title",
    fieldsets = (
        (None, {
            "fields": (
              "title",
              "description",
              "step",
              "time_limit",  
            ),
        }),
    )
    


    inlines = [
        CategoryInLine,
    ]

    def get_queryset(self, request):
        return Recipe.objects.prefetch_related("categories")


class RecipeInLine(admin.TabularInline):
    model = Category.recipes.through
    verbose_name_plural = "Добавить рецепты"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "description"
    ordering = "pk", "title",
    # search_fields = "pk", "title", "time_limit"
    fieldsets = (
        (None, {
            "fields": (
              "title",
              "description",
            ),
        }),
    )
    inlines = [
        RecipeInLine,
    ]

    def get_queryset(self, request):
        return Category.objects.prefetch_related("recipes")
