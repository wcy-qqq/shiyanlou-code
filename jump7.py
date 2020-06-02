for idx in range(1,101):
		if idx % 7 == 0:
			continue
		if idx % 10 == 7:
			continue
		if idx // 10 == 7:
			continue
		else:
			print(idx)

