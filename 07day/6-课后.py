weight = float(input("请输入体重"))
height = float(input("请输入身高"))
print(weight/(height)**2)
BMI = float(input("请输入BMI指数"))
if BMY < 18.5:
	print("过轻")
elif BMI >= 18.5 and BMI <25:
	print("过重")
elif BMI >=28 and BMI <32:
	print("肥胖")
elif BMI >= 32:
		print("严重肥胖")
