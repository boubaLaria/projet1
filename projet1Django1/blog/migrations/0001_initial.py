# Generated by Django 3.1.4 on 2020-12-08 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=50)),
                ('prenom_client', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=2)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_com', models.DateField(verbose_name='date published')),
                ('status', models.CharField(max_length=20)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.client')),
            ],
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_plat', models.CharField(max_length=100)),
                ('prix', models.IntegerField()),
                ('type_plat', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('commune', models.CharField(max_length=100)),
                ('quartier', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Repas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbr_plat', models.IntegerField()),
                ('id_cmd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.commande')),
                ('id_plat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.plat')),
            ],
        ),
        migrations.CreateModel(
            name='List_plat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_plat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.plat')),
                ('id_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.restaurant')),
            ],
        ),
    ]