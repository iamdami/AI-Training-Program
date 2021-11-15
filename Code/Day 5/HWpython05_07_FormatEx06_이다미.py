alignLeft="{1:<10}".format("niceday", "hi")
alignRight="{:>10}".format("niceday")
alignCenter="{0:^10}".format("niceday")

spaceFill01="{0:#^10}".format("hi")

print(alignLeft)
print(alignRight)
print(alignCenter)
print(spaceFill01)

x=3.12341234
y=3.43214321
floatEx1="{0:.4f} {1:f}".format(x, y)
floatEx2="{0:10.4f}".format(y)

print(floatEx1)
print(floatEx2)