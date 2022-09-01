count = 0
piggy_bank = 0

while piggy_bank < 15000:
	piggy_bank += piggy_bank * 0.01
	piggy_bank += 1000
	count += 1
	print(round(piggy_bank), count)
print(count)
