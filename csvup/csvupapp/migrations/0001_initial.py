# Generated by Django 4.2.3 on 2023-07-07 01:06

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Student')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='abrahamapp/file')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('prn', models.BigIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('branch', models.CharField(blank=True, max_length=500)),
                ('middle_name', models.CharField(blank=True, max_length=500)),
                ('gender', models.CharField(blank=True, max_length=500)),
                ('date_of_birth', models.DateField(blank=True)),
                ('year_of_admission', models.IntegerField(blank=True)),
                ('type_of_admission', models.CharField(blank=True, max_length=500)),
                ('want_college_placement', models.CharField(blank=True, max_length=500)),
                ('out_placement', models.CharField(blank=True, max_length=500)),
                ('personal_email', models.EmailField(blank=True, max_length=500)),
                ('college_email', models.EmailField(blank=True, max_length=500)),
                ('linkedin_url', models.URLField(blank=True)),
                ('mobile_number', models.BigIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)])),
                ('whatsapp_number', models.BigIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)])),
                ('alternate_number', models.BigIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)])),
                ('father_name', models.CharField(blank=True, max_length=500)),
                ('mother_name', models.CharField(blank=True, max_length=500)),
                ('permanent_address', models.CharField(blank=True, max_length=500)),
                ('current_address', models.CharField(blank=True, max_length=500)),
                ('ssc_percentage', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('diploma_student', models.CharField(blank=True, max_length=500)),
                ('sgpa_sy_sem1', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('sgpa_sy_sem2', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('sgpa_ty_sem1', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('sgpa_ty_sem2', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('sgpa_btech_sem1', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('sgpa_btech_sem2', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('sgpa_fy_sem1', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('sgpa_fy_sem2', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('hsc_percentage', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('diploma_percentage', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('gave_amcat_sy', models.CharField(blank=True, max_length=500)),
                ('gave_amcat_ty', models.CharField(blank=True, max_length=500)),
                ('avg_elq_sy', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('avg_elq_ty', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('have_backlog', models.CharField(blank=True, max_length=500)),
                ('live_backlog', models.CharField(blank=True, max_length=500)),
                ('dead_backlog', models.CharField(blank=True, max_length=500)),
                ('completed_certification', models.CharField(blank=True, max_length=500)),
                ('other_completed_certification', models.CharField(blank=True, max_length=500)),
                ('ongoing_certification', models.CharField(blank=True, max_length=500)),
                ('dropped_certification', models.CharField(blank=True, max_length=500)),
                ('fy_summer_internship', models.CharField(blank=True, max_length=500)),
                ('sy_summer_internship', models.CharField(blank=True, max_length=500)),
                ('ty_summer_internship', models.CharField(blank=True, max_length=500)),
                ('sponsored_project_industry', models.CharField(blank=True, max_length=500)),
                ('be_diploma_project_title', models.CharField(blank=True, max_length=500)),
                ('open_elective_specialisation', models.CharField(blank=True, max_length=500)),
                ('programming_languages_known', models.CharField(blank=True, max_length=500)),
                ('frameworks_known', models.CharField(blank=True, max_length=500)),
                ('software_known', models.CharField(blank=True, max_length=500)),
                ('languages_known', models.CharField(blank=True, max_length=500)),
                ('co_curricular_activities', models.CharField(blank=True, max_length=500)),
                ('special_achievements', models.CharField(blank=True, max_length=500)),
                ('scholarship', models.CharField(blank=True, max_length=500)),
                ('additional_details', models.CharField(blank=True, max_length=500)),
                ('extra_curricular_activities', models.CharField(blank=True, max_length=500)),
                ('preskillet_video_url', models.URLField(blank=True)),
                ('passport_size_url', models.URLField(blank=True)),
                ('sy_amcat_result_url', models.URLField(blank=True)),
                ('ty_amcat_result_url', models.URLField(blank=True)),
                ('all_industry_certification_url', models.URLField(blank=True)),
                ('all_education_certification_url', models.URLField(blank=True)),
                ('all_internship_certification_url', models.URLField(blank=True)),
                ('final_amcat_sy_url', models.URLField(blank=True)),
                ('final_amcat_ty_url', models.URLField(blank=True)),
                ('amcat_1', models.CharField(blank=True, max_length=500)),
                ('amcat_2', models.CharField(blank=True, max_length=500)),
                ('certification_done', models.CharField(blank=True, max_length=500)),
                ('eligible', models.CharField(blank=True, max_length=500)),
                ('awaiting', models.CharField(blank=True, max_length=500)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
