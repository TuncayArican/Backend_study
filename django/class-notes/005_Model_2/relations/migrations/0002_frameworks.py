# Generated by Django 4.0.4 on 2022-05-16 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frameworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relations.language')),
            ],
        ),
    ]
