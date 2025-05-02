Dict1 = {"Honda":1223,"Lada":789,"Bmw":788}#объявления словаря
Dict2 = {"Dog":9,"Cat":7,"Cow":12}#объявления словаря

Dict1.pop("Bmw")
Dict2.popitem()

Dict2.setdefault("Cat")

Dict1.update(Dict2)

Dict1.values()

Dict2.clear()

Dict1.copy()

Dict1.get("Lada")

Dict1.items()

keys_dict1 = Dict1.keys()
Values_dict1 = Dict1.values()
Dict1.keys()
Dict3 = {i:j for i,j in zip(keys_dict1,Values_dict1)}#генерация словаря
print(Dict3)