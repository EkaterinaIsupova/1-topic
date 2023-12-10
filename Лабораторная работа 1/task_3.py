# TODO Найдите количество книг, которое можно разместить на дискете


weight = 4
volume = 1.44
pages = 100
str_on_page = 50
symbols_in_str = 25
one_book = pages * str_on_page * symbols_in_str * weight
volume_in_bytes = volume * 1024 * 1024
count = int(volume_in_bytes // one_book)
print("Количество книг, помещающихся на дискету:", count)
