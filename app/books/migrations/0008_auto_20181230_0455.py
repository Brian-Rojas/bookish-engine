# Generated by Django 2.1.4 on 2018-12-30 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20181230_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
    ]