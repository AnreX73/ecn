# Generated by Django 4.1.4 on 2023-03-22 04:54

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
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
            name='User',
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
                ('phone_number', models.CharField(blank=True, max_length=30, verbose_name='телефон для связи')),
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
            name='Balcony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Балкон')),
            ],
            options={
                'verbose_name': 'Балкон',
                'verbose_name_plural': 'Балкон',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Bath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Баня')),
            ],
            options={
                'verbose_name': 'Баня',
                'verbose_name_plural': 'Баня',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BathroomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тип санузла')),
            ],
            options={
                'verbose_name': 'Тип санузла',
                'verbose_name_plural': 'Тип санузла',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='иллюстрация')),
                ('video', models.FileField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='видео (если есть)')),
                ('post', ckeditor.fields.RichTextField(blank=True, verbose_name='рекламная статья')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламные статьи',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CommercialObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='Основное изображение')),
                ('object_adress', models.CharField(blank=True, help_text='необязательно', max_length=255, verbose_name='адрес объекта')),
                ('square', models.PositiveIntegerField(blank=True, verbose_name='общая площадь кв.м')),
                ('live_square', models.PositiveIntegerField(blank=True, verbose_name='жилая площадь')),
                ('kitchen', models.PositiveIntegerField(blank=True, verbose_name='площадь кухни')),
                ('floor', models.PositiveIntegerField(blank=True, default=1, verbose_name='Этаж')),
                ('all_floor', models.PositiveIntegerField(blank=True, null=True, verbose_name='Этажность дома')),
                ('year', models.CharField(blank=True, max_length=25, verbose_name='Год постройки / Сдачи')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='текстовое описание ')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('bathroom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.bathroomtype', verbose_name='санузел')),
            ],
            options={
                'verbose_name': 'рекламный объект',
                'verbose_name_plural': 'Рекламные объекты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DistanceToCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.CharField(max_length=255, null=True, verbose_name='Расстояние до города')),
            ],
            options={
                'verbose_name': 'Расстояние до города',
                'verbose_name_plural': 'Расстояние до города',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Electricity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Электроснабжение')),
            ],
            options={
                'verbose_name': 'Электроснабжение',
                'verbose_name_plural': 'Электроснабжение',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ElevatorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тип лифта')),
            ],
            options={
                'verbose_name': 'Тип лифта',
                'verbose_name_plural': 'Тип лифта',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FlatState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Состояние')),
            ],
            options={
                'verbose_name': 'Состояние',
                'verbose_name_plural': 'Состояние',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ForestNearly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Лес рядом')),
            ],
            options={
                'verbose_name': 'Лес рядом',
                'verbose_name_plural': 'Лес рядом',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Гараж')),
            ],
            options={
                'verbose_name': 'Гараж',
                'verbose_name_plural': 'Гараж',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Gas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Газ')),
            ],
            options={
                'verbose_name': 'Газ',
                'verbose_name_plural': 'Газ',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='GoodRoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Асфальтовая дорога')),
            ],
            options={
                'verbose_name': 'Асфальтовая дорога',
                'verbose_name_plural': 'Асфальтовая дорога',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Graphics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='изображение')),
                ('description', models.CharField(max_length=55, verbose_name='описание изображения')),
                ('note', ckeditor.fields.RichTextField(blank=True, verbose_name='примечание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'графический объект',
                'verbose_name_plural': 'Графика и т.п.',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Greenhouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Теплица')),
            ],
            options={
                'verbose_name': 'Теплица',
                'verbose_name_plural': 'Теплица',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InCityObjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тип объекта')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('icon', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='иконка(картинка) для типа объекта')),
                ('in_main_page', models.BooleanField(default=True, verbose_name='в меню на главной странице')),
            ],
            options={
                'verbose_name': 'Тип объекта',
                'verbose_name_plural': 'Тип объекта',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InCityRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Район города')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Район города',
                'verbose_name_plural': 'Район города',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Landings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Посадки')),
            ],
            options={
                'verbose_name': 'Посадки',
                'verbose_name_plural': 'Посадки',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MetroStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Станция метро')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Станцию метро',
                'verbose_name_plural': 'Станция метро',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ObjectConstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='тип стройматериалов')),
            ],
            options={
                'verbose_name': 'тип стройматериалов',
                'verbose_name_plural': 'тип стройматериалов',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OutCityObjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тип загородного объекта')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('icon', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='иконка(картинка) для типа объекта')),
                ('in_main_page', models.BooleanField(default=True, verbose_name='в меню на главной странице')),
            ],
            options={
                'verbose_name': 'Тип загородного объекта',
                'verbose_name_plural': 'Тип загородного объекта',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Заголовок статьи')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='текст статьи')),
            ],
            options={
                'verbose_name': 'Статью',
                'verbose_name_plural': 'Статьи',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RoomAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_amount', models.PositiveIntegerField(default=1, unique=True, verbose_name='Кол-во комнат цифрами')),
                ('title', models.CharField(max_length=25, verbose_name='Количество комнат словами')),
                ('slug', models.SlugField(default='no_slug', max_length=150, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Количество комнат',
                'verbose_name_plural': 'Количество комнат',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Охрана')),
            ],
            options={
                'verbose_name': 'Охрана',
                'verbose_name_plural': 'Охрана',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ShopNearly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Магазин рядом')),
            ],
            options={
                'verbose_name': 'Магазин рядом',
                'verbose_name_plural': 'Магазин рядом',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeOfOwnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='форма собственности')),
            ],
            options={
                'verbose_name': 'форму собственности',
                'verbose_name_plural': 'форма собственности',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Вода')),
            ],
            options={
                'verbose_name': 'Вода',
                'verbose_name_plural': 'Вода',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WaterNearly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Водоем рядом')),
            ],
            options={
                'verbose_name': 'Водоем рядом',
                'verbose_name_plural': 'Водоем рядом',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WinterAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Доступ зимой')),
            ],
            options={
                'verbose_name': 'Доступ зимой',
                'verbose_name_plural': 'Доступ зимой',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OutCityObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Основное изображение')),
                ('is_hot', models.BooleanField(default=False, verbose_name='горячий вариант')),
                ('object_adress', models.CharField(blank=True, max_length=255, verbose_name='адрес объекта')),
                ('land_square', models.CharField(blank=True, max_length=50, verbose_name='площадь участка')),
                ('square', models.PositiveIntegerField(blank=True, help_text='в кв.м', verbose_name='площадь дома')),
                ('year', models.CharField(blank=True, max_length=25, verbose_name='год постройки')),
                ('transport_distance', models.CharField(blank=True, max_length=255, verbose_name='расстояние до транспорта')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='текстовое описание')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('bath', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.bath', verbose_name='Баня')),
                ('bathroom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.bathroomtype', verbose_name='Туалет')),
                ('city_distance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecn.distancetocity', verbose_name='расстояние до города')),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.objectconstruction', verbose_name='тип постройки')),
                ('electricity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.electricity', verbose_name='Электричество')),
                ('estate_agent', models.ForeignKey(help_text='специалист по объекту', on_delete=django.db.models.deletion.CASCADE, related_name='estate_agent', to=settings.AUTH_USER_MODEL, verbose_name='агент по недвижимости')),
                ('forest_nearly', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.forestnearly', verbose_name='Лес рядом')),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.garage', verbose_name='Гараж')),
                ('gas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.gas', verbose_name='Газ')),
                ('good_road', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.goodroad', verbose_name='Асфальтовая дорога')),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.greenhouse', verbose_name='Теплица')),
                ('landings', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.landings', verbose_name='Посадки')),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='obj_type', to='ecn.outcityobjecttype', verbose_name='тип объекта')),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.security', verbose_name='Охрана')),
                ('shop_nearly', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.shopnearly', verbose_name='Магазин рядом')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.flatstate', verbose_name='состояние')),
                ('type_of_ownership', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.typeofownership', verbose_name='форма собственности')),
                ('water', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.water', verbose_name='Вода')),
                ('water_nearly', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.waternearly', verbose_name='Водоем рядом')),
                ('winter_access', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.winteraccess', verbose_name='Доступ зимой')),
            ],
            options={
                'verbose_name': 'Загородный объект',
                'verbose_name_plural': 'Загородный объект',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InCityObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True, verbose_name='URL')),
                ('price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Основное изображение')),
                ('sale_or_rent', models.CharField(choices=[('s', 'Продажа'), ('r', 'Аренда')], default='s', max_length=25, verbose_name='Продажа или аренда')),
                ('is_hot', models.BooleanField(default=False, help_text='если хотите видеть на главной странице', verbose_name='горячий вариант')),
                ('object_adress', models.CharField(blank=True, help_text='необязательно', max_length=255, verbose_name='адрес объекта')),
                ('metro_distance', models.CharField(blank=True, max_length=255, verbose_name='расстояние до метро')),
                ('square', models.PositiveIntegerField(blank=True, verbose_name='общая площадь кв.м')),
                ('live_square', models.PositiveIntegerField(blank=True, verbose_name='жилая площадь')),
                ('kitchen', models.PositiveIntegerField(blank=True, verbose_name='площадь кухни')),
                ('rooms_layout', models.CharField(blank=True, max_length=255, verbose_name='планировка')),
                ('floor', models.PositiveIntegerField(blank=True, default=1, verbose_name='Этаж')),
                ('all_floor', models.PositiveIntegerField(blank=True, null=True, verbose_name='Этажность дома')),
                ('year', models.CharField(blank=True, max_length=25, verbose_name='Год постройки / Сдачи')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='текстовое описание ')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('balcony', models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='ecn.balcony', verbose_name='балкон')),
                ('bathroom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.bathroomtype', verbose_name='санузел')),
                ('city_region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='region', to='ecn.incityregion', verbose_name='район города')),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.objectconstruction', verbose_name='тип постройки')),
                ('elevator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.elevatortype', verbose_name='лифт')),
                ('estate_agent', models.ForeignKey(blank=True, default=1, help_text='специалист по объекту', on_delete=django.db.models.deletion.CASCADE, related_name='realtor', to=settings.AUTH_USER_MODEL, verbose_name='агент по недвижимости')),
                ('metro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.metrostation', verbose_name='станция метро')),
                ('object_type', models.ForeignKey(help_text='выберете тип объекта', on_delete=django.db.models.deletion.PROTECT, related_name='obj_type', to='ecn.incityobjecttype', verbose_name='тип объекта')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rooms', to='ecn.roomamount', verbose_name='количество комнат')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.flatstate', verbose_name='состояние')),
            ],
            options={
                'verbose_name': 'объект',
                'verbose_name_plural': 'объект в городе',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='GalleryComercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Фото')),
                ('note', models.CharField(blank=True, max_length=100, verbose_name='примечание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('gallery_com_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecn.commercialobject', verbose_name='Ссылка на объект')),
            ],
            options={
                'verbose_name': 'фото комерческого объекта',
                'verbose_name_plural': 'фото комерческих объектов',
                'ordering': ['gallery_com_link'],
            },
        ),
        migrations.CreateModel(
            name='Gallery2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image2', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Фото')),
                ('note2', models.CharField(blank=True, max_length=100, verbose_name='примечание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('galleryLink2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecn.outcityobject', verbose_name='Ссылка на объект')),
            ],
            options={
                'verbose_name': 'фото объекта',
                'verbose_name_plural': 'фото загородного объекта',
                'ordering': ['galleryLink2'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='Фото')),
                ('note', models.CharField(blank=True, max_length=100, verbose_name='примечание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('galleryLink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecn.incityobject', verbose_name='Ссылка на объект')),
            ],
            options={
                'verbose_name': 'фотографию объекта',
                'verbose_name_plural': 'фото объекта',
                'ordering': ['galleryLink'],
            },
        ),
        migrations.AddField(
            model_name='commercialobject',
            name='city_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='region_of_city', to='ecn.incityregion', verbose_name='район города'),
        ),
        migrations.AddField(
            model_name='commercialobject',
            name='construction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.objectconstruction', verbose_name='тип постройки'),
        ),
        migrations.AddField(
            model_name='commercialobject',
            name='elevator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecn.elevatortype', verbose_name='лифт'),
        ),
        migrations.AddField(
            model_name='commercialobject',
            name='estate_agent',
            field=models.ForeignKey(blank=True, help_text='специалист по объекту', on_delete=django.db.models.deletion.CASCADE, related_name='com_agent', to=settings.AUTH_USER_MODEL, verbose_name='агент по недвижимости'),
        ),
        migrations.AddField(
            model_name='commercialobject',
            name='post_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commercial_link', to='ecn.commercial', verbose_name='ссылка на статью'),
        ),
        migrations.AddField(
            model_name='commercialobject',
            name='rooms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rooms_amount', to='ecn.roomamount', verbose_name='количество комнат'),
        ),
    ]
