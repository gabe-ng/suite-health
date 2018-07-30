# Generated by Django 2.0.5 on 2018-07-30 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('kcal', models.CharField(max_length=100)),
                ('protein', models.CharField(max_length=100)),
                ('fat', models.CharField(max_length=100)),
                ('carbs', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='fitness_app.User')),
            ],
        ),
    ]