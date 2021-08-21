from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


STATUS_CHOICES = [
    ('new', 'Не модерировано'),
    ('moderated', 'Модерировано'),
    ('rejected', 'Отклонено')
]


class Advert(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок',
                             validators=[MinLengthValidator(10)])
    photo_img = models.ImageField(null=True, blank=True, upload_to='advert_pics', verbose_name='Картинка')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    price = models.DecimalField(null=True, blank=True, verbose_name='Цена', max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='adverts', verbose_name='Автор')
    category = models.ManyToManyField('webapp.Category', related_name='adverts', blank=True, verbose_name='Категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    publish_at = models.DateTimeField(verbose_name="Время публикации", blank=True, default=timezone.now)
    status = models.CharField(null=True, blank=True, max_length=15, choices=STATUS_CHOICES, default='new',
                              verbose_name='Статус')
    is_delete = models.BooleanField(default=False)

    def save(self, **kwargs):
        if not self.publish_at:
            if not self.pk:
                self.publish_at = timezone.now()
            else:
                self.publish_at = Advert.objects.get(pk=self.pk).publish_at
        super().save(**kwargs)

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        permissions = [('moderator', 'Модератор')]
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявлении'


class Category(models.Model):
    name = models.CharField(max_length=31, verbose_name='Категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
