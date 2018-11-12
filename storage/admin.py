from django.contrib import admin
from .models import UploadModel, DownloadModel, DeleteModel


admin.site.register([UploadModel, DownloadModel, DeleteModel])