# Generated by Django 4.1.7 on 2023-02-28 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('amenity_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_price', models.IntegerField()),
                ('description', models.TextField()),
                ('room_count', models.IntegerField(default=10)),
                ('amenities', models.ManyToManyField(to='home.amenities')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='hotel')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hotel', to='home.hotel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('booking_type', models.CharField(choices=[('pre paid', 'pre paid'), ('post paid', 'post paid')], max_length=100)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_booking', to='home.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
