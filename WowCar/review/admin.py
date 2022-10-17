from django.contrib import admin
from .models import *

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['car_model', 'reviewer', 'score', 'content', 'created_at']

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['review', 'commenter', 'comment', 'created_at']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)