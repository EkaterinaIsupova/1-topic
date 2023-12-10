users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
count = len(users)
unique_count = len(set(users))
dict_["Общее количество"] = count
dict_["Уникальные посещения"] = unique_count
print(dict_)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
