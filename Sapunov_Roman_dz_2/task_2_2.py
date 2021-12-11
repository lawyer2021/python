message = ["в", "5", "часов", "17", "минут", "температура", "воздуха", "была", "+5", "градусов"]
new_message = []
for i in message:
    if i.isdigit():
        i = int(i)
        new_message.append('"{:02d}"'.format(i))
    elif i.count("+") == 1:
        i = int(i)
        new_message.append('"+{:02d}"'.format(i))
    else:
        new_message.append(i)
print(" ".join(new_message))
