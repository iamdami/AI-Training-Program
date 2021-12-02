reader = ('케인', '손흥민', '홀란드', '음바페', '호날두', '반니', '케인', '반니', '카카', '드록바', '케인', '카카',
          '손흥민', '홀란드', '음바페', '호날두', '메시', '케인', '카카', '델리알리', '케인', '손흥민', '외질', '외질')

Name = 0
result = []
resultSet = {}

readerList = list(reader)

for Name in readerList:
    if len(Name) == 3:
        result.append(Name[1:len(Name)])
    elif len(Name) == 4:
        result.append(Name[2:len(Name)])
    else:
        result.append(Name)
print(result)

resultSet = set(result)
print(resultSet)
