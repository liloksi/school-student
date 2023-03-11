# Generated by Django 4.1.7 on 2023-03-11 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_city_name_alter_district_name_and_more'),
        ('online_queue', '0001_initial'),
        ('acievement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goldencertificate',
            name='points',
            field=models.IntegerField(verbose_name='оценки'),
        ),
        migrations.AlterField(
            model_name='goldencertificate',
            name='school_fullname',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.school', verbose_name='название школы'),
        ),
        migrations.AlterField(
            model_name='goldencertificate',
            name='student_fullname',
            field=models.OneToOneField(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='online_queue.student', verbose_name='имя студента'),
        ),
        migrations.AlterField(
            model_name='goldencertificate',
            name='year',
            field=models.IntegerField(verbose_name='год'),
        ),
        migrations.AlterField(
            model_name='olympiad',
            name='points',
            field=models.IntegerField(verbose_name='оценки'),
        ),
        migrations.AlterField(
            model_name='olympiad',
            name='school',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.school', verbose_name='школа'),
        ),
        migrations.AlterField(
            model_name='olympiad',
            name='student',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='online_queue.student', verbose_name='студент'),
        ),
        migrations.AlterField(
            model_name='olympiad',
            name='year',
            field=models.IntegerField(verbose_name='год'),
        ),
    ]