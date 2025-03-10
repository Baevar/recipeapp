# Generated by Django 5.1.6 on 2025-02-25 09:18

import django.db.models.deletion
import recipeapp.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Категория')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to=settings.AUTH_USER_MODEL, verbose_name='Автор категории')),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Рецепт')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание рецепта')),
                ('step', models.TextField(blank=True, null=True, verbose_name='Шаги приготовления')),
                ('time_limit', models.PositiveIntegerField(blank=True, default=0, verbose_name='Время приготовления')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to=recipeapp.models.recipe_preview_directory_path)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
                ('categories', models.ManyToManyField(blank=True, related_name='recipes', to='recipeapp.category', verbose_name='категории')),
            ],
            options={
                'verbose_name_plural': 'Рецепты',
                'ordering': ['title', 'time_limit'],
            },
        ),
    ]
