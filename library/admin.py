from django.contrib import admin
from .models import categoryModel, subCategoryModel, authorsModel, booksModel, CustomUser, commentsModel
# Register your models here.

admin.site.register(categoryModel)
admin.site.register(subCategoryModel)
admin.site.register(authorsModel)
admin.site.register(booksModel)
admin.site.register(CustomUser)
admin.site.register(commentsModel)
