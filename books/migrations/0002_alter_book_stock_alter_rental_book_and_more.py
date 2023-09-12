# Generated by Django 4.2.4 on 2023-09-12 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rental',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='books.book'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
