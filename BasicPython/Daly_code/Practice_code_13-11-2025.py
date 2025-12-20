bodmas = ((4*5)+10)/2-3**2
print('The result of the expression is:', bodmas)

bodmas_2 = (4%(1+5)**2-60//3+12)*2
print('The result of the second expression is:', bodmas_2)



input_str = 'Core_Python_program_2025'
print(input_str)
inputList = input_str.split('_')
print(inputList)




data_t = ('Mumbai', 100, 'Delhi', 200, 'Chennai', 300 )

#dt = [list(city, cityCode) for city, cityCode in range(0, len(data_t), 2)]
dt = [(data_t[i], data_t[i+1]) for i in range(0, len(data_t), 2)]
print(dt)

schema = ['City', 'CityCode']

data_dict = [dict(zip(schema, item)) for item in dt]
print(data_dict)