#1
immutable_var = 1, 'hello', True
print(immutable_var)
#2 Изменить нельзя так как присвоено значение кортежу 1 изначально
#immutable_var(int[0])= 5
#print(immutable_var)
immutable_var = ([1, 5], 4, 7)
immutable_var[0][0]=3
print(immutable_var)

#3
mutable_list = (1, 5, 'wer', 'qwerty', False)
my_string = ' '.join(map(str, mutable_list))
mutable_list = my_string + ' ' +str(78)
print(mutable_list)