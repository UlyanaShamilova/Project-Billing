# Generated by Django 4.2.5 on 2024-02-05 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth_reg", "0002_remove_userprofile_confirm_password_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
