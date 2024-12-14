# Generated by Django 5.1.2 on 2024-11-18 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='library',
            new_name='books',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='relationship_app.author'),
        ),
    ]