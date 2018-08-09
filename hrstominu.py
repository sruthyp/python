time = float(input("Input time in seconds: "))
hour = time //60
time %= 60
minutes = time // 1
print("h:m-> %d:%d" % (hour,minutes))
