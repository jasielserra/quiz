# Generated by Django 4.0 on 2022-01-03 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
