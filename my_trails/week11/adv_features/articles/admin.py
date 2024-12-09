from django.contrib import admin

# Register your models here.
from .models import JournalArticles
# this is possible 
# admin.site.register(JournalArticles)


#but we can also make the admin see other contents about the journal article instances

# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin   ..... this is used for custom user modles we made

class JournalArticlesAdmin(admin.ModelAdmin):
    list_display = ["title", "written_by", "written_date"]

admin.site.register(JournalArticles, JournalArticlesAdmin) # basically we are registering the modle on the admin plan and making certian things(defined above) display 

