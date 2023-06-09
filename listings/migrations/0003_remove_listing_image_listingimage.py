# Generated by Django 4.2.1 on 2023-05-21 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image',
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.listing')),
            ],
        ),
    ]
