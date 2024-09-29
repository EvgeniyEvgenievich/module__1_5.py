immutable_var_ = 1, 'Hello', True
print(immutable_var_)
#immutable_var_[0] = 1 # Кортеж относится к неизменяемым типам данных, поэтому нельзя изменить значения элементов кортежа
mutable_list_ = ['TicTac', False, 1888]
mutable_list_[1] = True
print(mutable_list_)
