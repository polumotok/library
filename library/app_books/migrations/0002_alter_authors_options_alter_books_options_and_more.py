# Generated by Django 4.0.1 on 2023-05-30 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_books", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="authors",
            options={"verbose_name": "author"},
        ),
        migrations.AlterModelOptions(
            name="books",
            options={"verbose_name": "book"},
        ),
        migrations.AlterModelOptions(
            name="genres",
            options={"verbose_name": "genre"},
        ),
        migrations.AlterModelOptions(
            name="shelves",
            options={"verbose_name": "shelve"},
        ),
        migrations.AddField(
            model_name="books",
            name="on_hands",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="authors",
            name="date_of_birth",
            field=models.DateField(null=True, verbose_name="дата рождения"),
        ),
        migrations.AlterField(
            model_name="authors",
            name="first_name",
            field=models.CharField(max_length=50, verbose_name="имя"),
        ),
        migrations.AlterField(
            model_name="authors",
            name="last_name",
            field=models.CharField(max_length=50, verbose_name="фамилия"),
        ),
        migrations.AlterField(
            model_name="books",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_books.authors",
                verbose_name="автор",
            ),
        ),
        migrations.AlterField(
            model_name="books",
            name="genre",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_books.genres",
                verbose_name="жанр",
            ),
        ),
        migrations.AlterField(
            model_name="books",
            name="publication",
            field=models.DateField(null=True, verbose_name="дата издания"),
        ),
        migrations.AlterField(
            model_name="books",
            name="shelves",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_books.shelves",
                verbose_name="полка",
            ),
        ),
        migrations.AlterField(
            model_name="books",
            name="title",
            field=models.CharField(max_length=100, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="genres",
            name="title",
            field=models.CharField(max_length=50, verbose_name="жанр"),
        ),
        migrations.AlterField(
            model_name="shelves",
            name="title",
            field=models.CharField(max_length=25, verbose_name="полка"),
        ),
    ]