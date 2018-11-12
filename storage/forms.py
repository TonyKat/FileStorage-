from django.forms import ModelForm
from .models import UploadModel, DownloadModel, DeleteModel


class UploadFileForm(ModelForm):
    class Meta:
        model = UploadModel
        fields = ['file_obj']


class DownloadFileForm(ModelForm):
    class Meta:
        model = DownloadModel
        fields = ['text_obj']


class DeleteFileForm(ModelForm):
    class Meta:
        model = DeleteModel
        fields = ['delete_obj']