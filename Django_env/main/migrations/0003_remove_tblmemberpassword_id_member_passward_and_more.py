# Generated by Django 4.1.3 on 2022-12-21 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tbladministrator_tblprojectattraction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblmemberpassword',
            name='id_member_passward',
        ),
        migrations.DeleteModel(
            name='TblAdminPassword',
        ),
        migrations.DeleteModel(
            name='TblMemberPassword',
        ),
    ]
