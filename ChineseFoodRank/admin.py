from django.contrib import admin
from ChineseFoodRank.models import Category,Food,FoodAdmin,Link,Vote,Style

# Add in this class to customized the Admin Interface
admin.site.register(Food,FoodAdmin)
admin.site.register(Category)
admin.site.register(Link)
admin.site.register(Vote)
admin.site.register(Style)



