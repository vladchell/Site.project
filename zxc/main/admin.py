from django.contrib import admin
from .models import *


class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PortfolioCatrgoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Contact)

admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(PortfolioCatrgory,PortfolioCatrgoryAdmin)