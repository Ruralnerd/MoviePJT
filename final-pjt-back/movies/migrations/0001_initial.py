# Generated by Django 3.1.7 on 2021-05-27 15:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('original_language', models.TextField(blank=True)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.CharField(max_length=150)),
                ('overview', models.TextField(blank=True)),
                ('popularity', models.FloatField(blank=True)),
                ('poster_path', models.CharField(blank=True, max_length=255)),
                ('release_date', models.DateField(blank=True)),
                ('vote_average', models.FloatField(blank=True)),
                ('vote_count', models.IntegerField(blank=True)),
                ('genre_ids', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('opinion', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
