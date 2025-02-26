from django.core.management import BaseCommand
from recipeapp.models import Recipe


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create recipes")
        recipe_names = ["Яичница",
                        "Каша",
                        ]
        for recipe_name in recipe_names:
            recipe, created = Recipe.objects.get_or_create(title=recipe_name)
            self.stdout.write(f"Create recipe {recipe.title}")
        self.stdout.write("SUCCESS!!")
