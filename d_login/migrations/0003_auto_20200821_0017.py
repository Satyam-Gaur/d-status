# Generated by Django 3.1 on 2020-08-20 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('d_login', '0002_auto_20200818_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('t_factor', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
