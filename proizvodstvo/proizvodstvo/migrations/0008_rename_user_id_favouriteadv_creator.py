# Generated by Django 4.1.7 on 2023-03-03 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proizvodstvo', '0007_rename_user_favouriteadv_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favouriteadv',
            old_name='user_id',
            new_name='creator',
        ),
    ]
