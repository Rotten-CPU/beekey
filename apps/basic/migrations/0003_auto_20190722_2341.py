# Generated by Django 2.2.3 on 2019-07-22 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20190722_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='bannerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='轮播描述')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('state', models.BooleanField(default=True, verbose_name='是否展示')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播商品',
                'verbose_name_plural': '轮播商品',
            },
        ),
        migrations.AlterField(
            model_name='basicmodel',
            name='companyAdress',
            field=models.CharField(default=1, max_length=100, verbose_name='公司地址'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicmodel',
            name='companyLink',
            field=models.CharField(default=1, max_length=100, verbose_name='联系人'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicmodel',
            name='companyLinkPhone',
            field=models.CharField(default=1, max_length=100, verbose_name='联系电话/微信'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicmodel',
            name='companyName',
            field=models.CharField(default=1, max_length=100, verbose_name='公司名称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicmodel',
            name='logoPic',
            field=models.ImageField(default=1, upload_to='logo/', verbose_name='Logo'),
            preserve_default=False,
        ),
    ]
