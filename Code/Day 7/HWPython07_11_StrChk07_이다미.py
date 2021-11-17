a = "20211117Rainy"
Vdate = a[:8]
Vweather = a[8:]
Vyear = a[:4]
Vmonth = a[4:6]
Vday = a[6:8]

print(f'날짜: {Vdate}')
print(f'날씨: {Vweather}')
print(f'년: {Vyear}')
print(f'월: {Vmonth}')
print(f'일: {Vday}')
