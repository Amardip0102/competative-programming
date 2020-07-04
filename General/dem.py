import re
abc_list = ['1.png', '5.png', '3.png', '4.png', '2.png', '8.png', '7.png', '9.png', '6.png', '11.png', '10.png']
'''

new_list = sorted([int(abc_list[i].rstrip('.png')) for i in range(len(abc_list)) if '.png' in abc_list[i]])
new_list = [str(new_list[i]) + '.png' for i in range(len(new_list))]

print(new_list)
'''
# abc_list.sort(key=lambda f: int(re.sub('\D', '', f)))
print(abc_list)