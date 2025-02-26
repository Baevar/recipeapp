from recipeapp.models import Category, Recipe
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

class RecipeForm(ModelForm):
    categories = ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Recipe
        fields = ["title", "description", "step", "time_limit", "categories","preview_image"]

    def save(self, commit=True):
        recipe = super().save(commit=False)
        if commit:
            recipe.save()
            self.save_m2m()  
        return recipe