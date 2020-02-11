from django.contrib import admin
from .models import Question, Choice, Person, Group, Membership
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)

