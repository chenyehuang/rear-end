# Generated by Django 4.2 on 2023-05-28 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product_referrer_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercollect',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='usercollect',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='usercollect',
            name='user_id',
        ),
        migrations.AlterUniqueTogether(
            name='uservalue',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='uservalue',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='uservalue',
            name='user_id',
        ),
        migrations.AlterUniqueTogether(
            name='userview',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userview',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='userview',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='UserCollect',
        ),
        migrations.DeleteModel(
            name='UserValue',
        ),
        migrations.DeleteModel(
            name='UserView',
        ),
    ]