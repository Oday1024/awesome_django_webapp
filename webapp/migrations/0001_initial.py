# Generated by Django 2.0.2 on 2018-02-07 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_image', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_image', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Blogs')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('admin', models.IntegerField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Users'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Users'),
        ),
    ]
