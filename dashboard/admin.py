from django.contrib import admin
from dashboard.models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'test_date')
    list_filter = ('test_date',)
    search_fields = ('id', 'user_id__username', 'test_date')
    list_display_links = ('id', 'user_id')
    ordering = ('-test_date',)

admin.site.site_header = "Адміністрування Тестів"
admin.site.site_title = "Тести"  
admin.site.index_title = "Управління Тестами" 


admin.site.register(Test, TestAdmin)
