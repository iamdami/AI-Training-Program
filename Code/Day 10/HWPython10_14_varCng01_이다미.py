var01=100
var02=200
print("변경 전 var01:", var01 )
print("변경 전 var02:", var02)

print("="*20)

var01 = var02
print("변경 후 var01:", var01 )
print("변경 후 var02:", var02)

print("="*20)


var01=100
var02=200

tmp = var01
var01 = var02
var02 = tmp

print("tmp 저장 후 var01:", var01 )
print("tmp 저장 후 var02:", var02)