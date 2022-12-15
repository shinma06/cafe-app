from django.contrib import admin
'''
作成したモデルを管理画面に反映するファイル
'''
from .models import News, Menu

admin.site.register(News)

admin.site.register(Menu)