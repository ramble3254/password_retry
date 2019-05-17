password = 'a123456'
times = 3
while times > 0:
	times = times - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if times > 0:
			print('還有', times, '次機會')
		else:
			print('沒機會了!')