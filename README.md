# Gray_filter Отчет
Результат работы профилирования filter.py – 25,8 секунд
![alt text](pictures_for_readme/filter_profile.JPG)
Результат профилирования old_filter.py – 33,8 секунд
![alt text](pictures_for_readme/old_filter_profile.JPG)
Несмотря на большее количество вызовов новый фильтр работает быстрее

Теперь сделаем выполнение нового фильтра filter.py автоматическим,т.е. без ввода пользователем в консоль значений.
Создадим новый файл filter_with_filename.py, в котором сразу в коде укажем имена файлов исходного и результирующего,
а также размер сетки 10 и количество градаций серого 50

-консольный ввод в filter.py 
![atl text](pictures_for_readme/filter_console_enter.JPG)
-заполненные в коде параметры в filter_with_filename.py, избавляющие от консольного ввода
![alt text](pictures_for_readme/filter_with_filename_without_console_enter.JPG)

На выполнение filter_with_filename.py ушли рекордные 1,8 сек.
(Так как больше не затрачивается время на сбор информации от пользователя)
![alt text](pictures_for_readme/filter_with_filename_profile.JPG)

За тестовое изображение я взяла свой рисунок
![alt text](test.jpg)

Результат работы изначального фильтра old_filter.py:
![alt text](res_old.jpg)

Результат работы фильтра filter.py, с введенными значениями:
размер сетки - 5
количество градаций серого - 5:
![alt text](res.jpg)

Результат работы фильтра filter_with_filename.py(размер сетки 10, 50 градаций серого):
![atl text](res_with_filename.jpg)