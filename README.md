# FileStorage-

Upload:
- получив файл от клиента, файл сохраняется на диск в следующую структуру каталогов:
store/с6/с6ag5jsh6...
где "с6ag5jsh6..." - имя файла, совпадающее с его хэшем.
/c6/ - подкаталог, состоящий из первых двух символов хэша файла.

Download:
- Запрос на скачивание: клиент передаёт параметр - хэш файла. Ищется
файл в локальном хранилище и отдается, если файл найден.

Delete:
- Запрос на удаление: клиент передаёт параметр - хэш файла. Ищется
файл в локальном хранилище и удаляется, если файл найден.

__________________________________________________________________________________________
Для запуска django-проекта: python manage.py runserver.

Версия Django: 2.1.3.
