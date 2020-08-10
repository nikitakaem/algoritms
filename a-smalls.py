
#countdown
def countdown(i):
	while i > 1:
		x = "finish"
		i -= 1
		print (i)
	return x



print(countdown(9))

def countdown2(i):
	print(i)
	if i <= 0:
		return
	else:
		countdown2(i - 1)

print(countdown2(9))


#factorial (recursion)
def sb(x):
    if x == 1:
        return 1
    else:
      return x * sb(x - 1)

print(sb(6))