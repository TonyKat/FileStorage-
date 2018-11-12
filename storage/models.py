from django.db import models

from storage.myfunctions import hash_upload


class UploadModel(models.Model):
    file_obj = models.FileField(upload_to=hash_upload, verbose_name='Загрузка файла')


class DownloadModel(models.Model):
    text_obj = models.CharField(verbose_name='Введите хэш файла для скачивания', max_length=32,
                                default='')


class DeleteModel(models.Model):
    delete_obj = models.CharField(verbose_name='Введите хэш удаляемого файла', max_length=32,
                                  default='')