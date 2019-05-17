password = 'a123456'
times = 3
while times > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		times = times - 1
		print('密碼錯誤,還有', times, '次機會')
		if times == 0:
			break