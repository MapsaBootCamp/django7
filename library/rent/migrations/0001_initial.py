# Generated by Django 4.0.4 on 2022-05-05 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField(auto_now_add=True)),
                ('return_bayad_date', models.DateField()),
                ('return_avorde_date', models.DateField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.profile')),
            ],
        ),
    ]