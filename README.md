# Gray_filter Отчет
Результат работы профилирования filter.py – 25,8 секунд
![alt text](pictures_for_readme/filter_profile.JPG)
Результат профилирования old_filter.py – 33,8 секунд
![alt text](pictures_for_readme/old_filter_profile.JPG)
Несмотря на большее количество вызовов новый фильтр работает быстрее

Теперь сделаем выполнение нового фильтра filter.py автоматическим,т.е. без ввода пользователем в консоль значений.
Создадим новый файл filter_with_filename.py, в котором сразу в коде укажем имена файлов исходного и результирующего,
а также размер сетки 10 и количество градаций серого 50
![alt text](pictures_for_readme/filter_with_filename_profile.JPG)
