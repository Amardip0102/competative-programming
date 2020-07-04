from collections import OrderedDict
n = int(input())
supermarket = OrderedDict()

for _ in range(int(n)):
    item_name, space, net_price  = input().rpartition(" ")
    supermarket[item_name] = supermarket.get(item_name, 0) + int(net_price)

for item, quantity in supermarket.items():
    print(item, quantity)


