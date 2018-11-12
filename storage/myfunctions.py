import hashlib
import os
from os.path import isfile, isdir, join
from django_project.settings import MEDIA_ROOT


def find_for_download_file(download_data, name_func):
    path = MEDIA_ROOT
    dirs = [join(path, one_dir) + '/' for one_dir in os.listdir(path) if isdir(join(path, one_dir))]
    for one_dir in dirs:
        if one_dir[-3:-1] == download_data[0:2]:
            for one_file in os.listdir(one_dir):
                file = join(one_dir, one_file)
                if isfile(file):
                    if one_file.split('.')[0] == download_data:
                        if name_func == 'delete':
                            return one_file, file, len(os.listdir(one_dir))
                        return one_file, file
    if name_func == 'delete':
        return '', '', 0
    else:
        return '', ''


def read_file_bytes(instance):
    instance.open()
    instance.seek(0)
    file = b''
    for chunk in iter(lambda: instance.read(4096), b''):
        file += chunk
    return file


def get_hash(instance):
    file = read_file_bytes(instance)
    hash_md5 = hashlib.md5()
    hash_md5.update(file)
    return hash_md5.hexdigest()


def hash_upload(instance, filename):
    hash_item = get_hash(instance.file_obj)
    fname, ext = os.path.splitext(filename)
    return '{0}/{1}{2}'.format(hash_item[0:2], hash_item, ext)
