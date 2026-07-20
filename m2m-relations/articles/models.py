from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название тега', unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    # Связь через промежуточную модель Scope
    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    """
    Промежуточная модель связи Статья <-> Тег.
    Здесь хранится признак основного раздела (is_main).
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной раздел')

    class Meta:
        verbose_name = 'Связь статьи и тега'
        verbose_name_plural = 'Связи статей и тегов'
        # Чтобы в шаблоне article.scopes.all() отдавал удобный порядок,
        # можно задать порядок по умолчанию: сначала основной, потом остальные по имени тега.
        ordering = ['-is_main', 'tag__name']

    def __str__(self):
        return f'{self.article.title} — {self.tag.name} {"(основной)" if self.is_main else ""}'