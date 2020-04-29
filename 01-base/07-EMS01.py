user_list = [
	'张三\t男\t18\t北京',
	'屠娇娇\t女\t22\t北京',
	'肖锋\t男\t34\t北京',
	'风四娘\t女\t32\t北京'
	]

print("*"*20, "欢迎来到员工管理系统", "*"*20)

while True :
	print("请选择你的操作:")
	print("\t1.查询员工")
	print("\t2.添加员工")
	print("\t3.删除员工")
	print("\t4.退出系统")
	print("*"*62)

	select = int(input("请选择[1-4]:"))

	if select == 1 :
		print("*"*62)
		print("\t序号\t姓名\t性别\t年龄\t城市")
		index = 1
		for user in user_list :
			print(f"\t{index}\t{user}")
			index += 1
	elif select == 2 :
		print("请输入要添加的员工信息:")
		name = input("姓名:")
		gender = input("性别:")
		age = input("年龄:")
		city = input("城市:")
		user_list.append(f"{name}\t{gender}\t{age}\t{city}")
		print("添加成功")
	elif select == 3 :
		del_num = int(input("请选择要删除的员工编号:"))
		if del_num <= len(user_list) :
			print("员工信息:")
			print(f"\t{del_num}\t{user_list[del_num - 1]}")
			is_del = input( "请确认是否删除[y/n]:")
			if is_del == 'y' :
				del user_list[del_num - 1]
				print("删除成功")
			else :
				print("放弃删除！")
		else :
			print("员工不存在！请确认操作")
	elif select == 4 :
		print("欢迎使用！再见！\n")
		break
	else :
		print("输入无效！！！请重新选择")
	print("*"*62)
