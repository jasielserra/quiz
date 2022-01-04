# Generated by Django 3.2.10 on 2022-01-01 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField()),
                ('alternativas', models.JSONField()),
                ('disponivel', models.BooleanField(default=False)),
                ('alternativa_correta', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')])),
            ],
        ),
    ]
