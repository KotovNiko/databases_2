from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # В list_display НЕЛЬЗЯ ставить teachers (ManyToMany). Ставим метод teachers_list.
    list_display = ('name', 'group', 'teachers_list')

    def teachers_list(self, obj):
        """Возвращает строку со всеми учителями студента через запятую."""
        return ", ".join(teacher.name for teacher in obj.teachers.all())

    teachers_list.short_description = "Учителя"


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
