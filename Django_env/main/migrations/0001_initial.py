# Generated by Django 4.1.3 on 2022-12-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAttraction',
            fields=[
                ('id_attraction', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('detail', models.CharField(max_length=2000)),
                ('picture', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'tbl_attraction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCity',
            fields=[
                ('id_city', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tbl_city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMember',
            fields=[
                ('id_member', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('gmail', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'tbl_member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblProject',
            fields=[
                ('id_project', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField()),
                ('modify_time', models.DateTimeField(blank=True, null=True)),
                ('statrt_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'tbl_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMemberPassword',
            fields=[
                ('id_member_passward', models.OneToOneField(db_column='id_member_passward', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.tblmember')),
                ('normal_pswd', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tbl_member_password',
                'managed': False,
            },
        ),
    ]
