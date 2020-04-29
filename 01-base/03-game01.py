# 唐僧大战白骨精

# 1- 欢迎界面
print("欢迎来到僧精峡谷~~~")
print("请选择你的身份:")
print("\t1.唐僧")
print("\t2.白骨精")
index = int(input("请选择:"))

life = 50
weight = 65

lianji = "1.练级"
daguai = "2.打怪"
taopao = "3.逃跑"

bgj_life = 20
bgj_weight = 25

# 2- 选择操作界面
if index == 1 :
	print("-----------------------------")
	print("你选择的身份是唐僧！你的生命值是2，武力值是2")
	print("下面请开始你的游戏吧")
	print("-----------------------------")
elif index == 2 :
	print("-----------------------------")
	print("哎呀，白骨精不喜欢你的呐~")
	print("系统自动为你分配了唐僧的身份！你的生命值是2，武力值是2")
	print("下面请开始你的游戏吧")
	print("-----------------------------")
else :
	print("-----------------------------")
	print("哎呀，要乖喔~")
	print("系统自动为你分配了唐僧的身份！你的生命值是2，武力值是2")
	print("下面请开始你的游戏吧")
	print("-----------------------------")

while life > 0 and weight > 0 :
	print("请选择你想要的操作")
	print(f"\t{lianji}")
	print(f"\t{daguai}")
	print(f"\t{taopao}")
	choose = int(input())
	if choose == 1 :
		print("****************")
		print(f"你选择的操作是{lianji}！你的生命值提升为{life + 2}，武力值提升为{weight + 3}")
		print("****************")
		life += 2
		weight += 3
	elif choose == 2 :
		print("****************")
		print(f"你选择的操作是{daguai}!")
		print(f"目前你的生命值为{life}，武力值为{weight}!")
		print("战斗中~~~~~")
		while life > 0 and weight > 0:
			if life < bgj_life and weight < bgj_weight :
				life = 0
				weight = 0
				print("阿欧！你太菜啦~一下子就被打败啦~回去好好练级呦~~~")
				print("****************")
			elif life > bgj_life or weight > bgj_weight :
				print("激烈战斗中~~~~")
				life -= 4
				weight -= 6
			bgj_life -= 4
			bgj_weight -= 5
		print("白骨精太厉害啦~~~~你失败啦~~~")
		print("游戏结束，咩咩咩~~~")
	elif choose == 3 :
		print("****************")
		print("哎呀~，怎么临阵脱逃了呢~~~")
		print("游戏结束，呜呜呜~~~")
		life = 0
		weight = 0
	else :
		print("输入错误，请重新选择！")
	
