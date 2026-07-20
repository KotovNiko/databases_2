from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()

        # Считаем, сколько форм помечено как is_main
        main_count = 0
        for form in self.forms:
            # Если форма не удалена и помечена как основная
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_main'):
                    main_count += 1

        if main_count == 0:
            raise ValidationError('У статьи должен быть ровно один основной раздел (is_main).')
        if main_count > 1:
            raise ValidationError('У статьи может быть только один основной раздел (is_main).')


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
