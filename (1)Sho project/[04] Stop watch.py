import time

output = float(0.00) #วิและนาที
hour = int(0) #ตัวบอกชม.
t_m = int(0) #ตัวบอกจำนวนวิเพื่อเปลี่ยนเป็นนาที
t_h = int(0) #ตัวบอกจำนวนนาทีเพื่อเปลี่ยนเป็นชม.

start = int(0)
while start != 1:
    time.sleep(1)
    output = output + float(0.01)
    t_m = t_m + int(1)
    print('[%d hour] %.2f min' %(hour,output))
    if t_m == int(60): #func change in to min
        output = output - float(0.60)#เปลี่ยนเป็นนาที
        output = output + float(1.00)
        t_h = t_h + int(1)
        t_m = t_m - t_m #close
    elif t_h == int(60):#print the hour
        hour = hour + int(1)
        output = output - float(60.00)
        print('[%d hour] %.2f min' %(hour,output))
        t_h = t_h - t_h#close