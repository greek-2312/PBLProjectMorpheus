# Generated by Django 3.1.2 on 2020-12-12 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('IDS', models.FloatField(default=1.0)),
                ('Sleep_Quality', models.FloatField(default=1.0)),
                ('hour0_Real', models.IntegerField(default=0)),
                ('hour1_Real', models.IntegerField(default=0)),
                ('hour2_Real', models.IntegerField(default=0)),
                ('hour3_Real', models.IntegerField(default=0)),
                ('hour4_Real', models.IntegerField(default=0)),
                ('hour5_Real', models.IntegerField(default=0)),
                ('hour6_Real', models.IntegerField(default=0)),
                ('hour7_Real', models.IntegerField(default=0)),
                ('hour8_Real', models.IntegerField(default=0)),
                ('hour9_Real', models.IntegerField(default=0)),
                ('hour10_Real', models.IntegerField(default=0)),
                ('hour11_Real', models.IntegerField(default=0)),
                ('hour12_Real', models.IntegerField(default=0)),
                ('hour13_Real', models.IntegerField(default=0)),
                ('hour14_Real', models.IntegerField(default=0)),
                ('hour15_Real', models.IntegerField(default=0)),
                ('hour16_Real', models.IntegerField(default=0)),
                ('hour17_Real', models.IntegerField(default=0)),
                ('hour18_Real', models.IntegerField(default=0)),
                ('hour19_Real', models.IntegerField(default=0)),
                ('hour20_Real', models.IntegerField(default=0)),
                ('hour21_Real', models.IntegerField(default=0)),
                ('hour22_Real', models.IntegerField(default=0)),
                ('hour23_Real', models.IntegerField(default=0)),
                ('hour0_Generated', models.IntegerField(default=0)),
                ('hour1_Generated', models.IntegerField(default=0)),
                ('hour2_Generated', models.IntegerField(default=0)),
                ('hour3_Generated', models.IntegerField(default=0)),
                ('hour4_Generated', models.IntegerField(default=0)),
                ('hour5_Generated', models.IntegerField(default=0)),
                ('hour6_Generated', models.IntegerField(default=0)),
                ('hour7_Generated', models.IntegerField(default=0)),
                ('hour8_Generated', models.IntegerField(default=0)),
                ('hour9_Generated', models.IntegerField(default=0)),
                ('hour10_Generated', models.IntegerField(default=0)),
                ('hour11_Generated', models.IntegerField(default=0)),
                ('hour12_Generated', models.IntegerField(default=0)),
                ('hour13_Generated', models.IntegerField(default=0)),
                ('hour14_Generated', models.IntegerField(default=0)),
                ('hour15_Generated', models.IntegerField(default=0)),
                ('hour16_Generated', models.IntegerField(default=0)),
                ('hour17_Generated', models.IntegerField(default=0)),
                ('hour18_Generated', models.IntegerField(default=0)),
                ('hour19_Generated', models.IntegerField(default=0)),
                ('hour20_Generated', models.IntegerField(default=0)),
                ('hour21_Generated', models.IntegerField(default=0)),
                ('hour22_Generated', models.IntegerField(default=0)),
                ('hour23_Generated', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
