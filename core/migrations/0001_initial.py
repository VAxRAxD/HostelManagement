# Generated by Django 4.0 on 2022-01-22 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Occupied', 'Occupied'), ('Empty', 'Empty')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_details', to='core.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_details', to='core.student'),
        ),
    ]
