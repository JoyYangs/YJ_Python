# 唐僧大战白骨精
# 优化版

player = "唐僧"
boss = "白骨精"

# 1- 欢迎界面
print("-"*20,"欢迎来到 * 王者峡谷 *","-"*20)
print("请选择你的身份:")
print(f"\t1.{player}")
print(f"\t2.{boss}")
index = int(input("请选择[1-2]:"))

player_life = 2
player_attack = 2

lianji = "练级"
daguai = "打怪"
taopao = "逃跑"

boss_life = 20
boss_attack = 25

print("-"*63)

# 2- 选择操作界面
if index == 1 :
	print(f"你选择的身份是[{player}]！你的生命值是2，武力值是2")
	print("下面请开始你的游戏吧")
elif index == 2 :
	print(f"哎呀，[{boss}]不喜欢你的呐~")
	print(f"系统自动为你分配了[{player}]的身份！你的生命值是2，武力值是2")
	print("下面请开始你的游戏吧")
else :
	print("哎呀，要乖喔~")
	print(f"系统自动为你分配了[{player}]的身份！你的生命值是2，武力值是2")
	print("下面请开始你的游戏吧")

while True:
	print("-"*63)
	print("请选择你想要的操作")
	print(f"\t1.{lianji}")
	print(f"\t2.{daguai}")
	print(f"\t3.{taopao}")
	choose = int(input())
	if choose == 1 :
		print("-"*63)
		print(f"你选择的操作是1.{lianji}!")
		player_life += 2
		player_attack += 3
		print(f"恭喜你升级成功！你的生命值提升为{player_life}，武力值提升为{player_attack}")
	elif choose == 2 :
		print("-"*63)
		print(f"你选择的操作是2.{daguai}!")
		print(f"目前你的生命值为{player_life}，武力值为{player_attack}!")
		print("战斗中~~~~~")
		boss_life -= player_attack
		if boss_life <= 0 :
			print(f"哇哦~~~ {boss} 在你的攻击下受到了 {player_attack} 点伤害败北了！恭喜你胜利啦~~~")
		else :
			print("阿欧！你太菜啦~一下子就被打败啦~回去好好练级呦~~~")
		print("游戏结束，咩咩咩~~~")
		break
	elif choose == 3 :
		print("-"*63)
		print(f"你选择的操作是2.{taopao}!")
		print("哎呀~，怎么临阵脱逃了呢~~~")
		print("游戏结束，呜呜呜~~~")
	else :
		print("输入错误，请重新选择！")
	
