# Generated by Django 2.2.3 on 2019-07-22 23:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='站点名称')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '站点设置',
                'verbose_name_plural': '站点设置',
            },
        ),
    ]
