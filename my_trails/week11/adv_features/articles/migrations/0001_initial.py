# Generated by Django 5.1.2 on 2024-11-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JournalArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('written_by', models.CharField(max_length=100)),
                ('written_date', models.DateField()),
            ],
            options={
                'permissions': [('can_view', 'can view articles'), ('can_create', 'can create articles'), ('can_edit', 'can edit articles'), ('can_delete', 'can delete articles')],
            },
        ),
    ]