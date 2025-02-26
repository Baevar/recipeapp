from django.core.management import BaseCommand
from recipeapp.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Создание категорий:")
        category_names = [
            "Завтрак",
            "Обед",
        ]
        
        for category_name in category_names:
            category, created = Category.objects.get_or_create(title=category_name)
            self.stdout.write(f"Создана категория {category.title}")
        self.stdout.write("Успешно!")
    