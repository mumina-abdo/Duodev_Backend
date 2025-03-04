# Generated by Django 4.2.16 on 2024-09-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('post_textilebale_custom', 'Can post textile bale'), ('buy_textilebale', 'Can buy textile bale'), ('view_textilebale_custom', 'Can view textile bale')]},
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
