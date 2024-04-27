from django.contrib import admin

from takeTest.models import Result

class ResultAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','test')
    list_filter = ('test',)
    search_fields = ('test',)
    list_display_links = ('first_name', 'last_name','test')
    ordering = ('-test',)

admin.site.site_header = "Адміністрування Результатами"
admin.site.site_title = "Результати"  
admin.site.index_title = "Управління Результатами" 


admin.site.register(Result, ResultAdmin)
