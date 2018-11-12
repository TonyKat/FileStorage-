import os
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from .forms import UploadFileForm, DownloadFileForm, DeleteFileForm
from .myfunctions import find_for_download_file, get_hash


def main_menu(request):
    return render(request, 'storage/main.html', {})


def delete_file(request):
    delete_form = DeleteFileForm()
    if request.method == 'POST':
        delete_data = request.POST.get('delete_obj')
        file_name, path_to_file, number_of_files_in_directory = find_for_download_file(delete_data, 'delete')
        if number_of_files_in_directory > 1:
            os.remove(path_to_file)
        elif number_of_files_in_directory == 1:
            os.remove(path_to_file)
            os.rmdir(path_to_file[:len(path_to_file) - len(file_name)])

        return render(request, 'storage/delete_file.html', {'delete_data': delete_form,
                                                            'success': 'успешно',
                                                            'file_name': file_name,
                                                            'hash_file': delete_data})
    else:
        return render(request, 'storage/delete_file.html', {'delete_data': delete_form})


def download_file(request):
    if request.method == 'POST':
        download_data = request.POST.get('text_obj')
        file_name, path_to_file = find_for_download_file(download_data, 'download')
        if file_name == '':
            return render(request, 'storage/not_found_file.html', {})
        else:
            with open(path_to_file, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/force-download')
                response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
                response['X-Sendfile'] = smart_str(path_to_file)
                return response
    else:
        download_form = DownloadFileForm()
        return render(request, 'storage/download_file.html', {'download_data': download_form})


def upload_file(request):
    if request.method == 'POST':
        hash_item = get_hash(request.FILES.get('file_obj'))
        upload_data = UploadFileForm(request.POST, request.FILES)
        if upload_data.is_valid():
            upload_data.save()
            return render(request, 'storage/upload_file.html', {'upload_data': upload_data,
                                                                'hash_item': hash_item,
                                                                'file_name': request.FILES.get('file_obj')})
        else:
            return HttpResponse('Invalid data')
    else:
        upload_data = UploadFileForm()
    hash_item = ''
    return render(request, 'storage/upload_file.html', {'upload_data': upload_data,
                                                        'hash_item': hash_item})