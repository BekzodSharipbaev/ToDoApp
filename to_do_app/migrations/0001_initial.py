# Generated by Django 4.2.3 on 2023-07-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.PositiveSmallIntegerField(choices=[[1, 'Low'], [2, 'Medium'], [3, 'High']], default=1)),
                ('status', models.BooleanField(choices=[[True, 'Done'], [False, 'In Progress']], default=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('status', 'deadline', '-priority'),
            },
        ),
    ]
