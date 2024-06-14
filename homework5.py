immutable_var = 1, 2, 3, True, 'apple'
print(immutable_var )
#элементы кортежей менять нельзя – это неизменяемый тип данных, при попытке изменить элементы в кортеже программа будет выдавать ошибку
mutable_list = [ 'red' , 'blue', 'green']
print(mutable_list)
mutable_list [1] = 'yellow'
mutable_list.extend (['white',2])
mutable_list.append ("black")
mutable_list.remove('red')
print (mutable_list)