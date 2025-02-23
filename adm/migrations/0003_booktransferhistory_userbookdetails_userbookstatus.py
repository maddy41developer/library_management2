# Generated by Django 5.0.6 on 2024-07-20 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_studentdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booktransferhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('book_name', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.studentdetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserBookDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.studentdetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserBookStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.bookdetails')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.studentdetails')),
            ],
        ),
    ]
