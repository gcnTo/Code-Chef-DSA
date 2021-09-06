def adder(box, total, initial_minimum):
    if len(box) == 1:
        return total + box[0] - initial_minimum
    else:
        smallest = min(box)
        pos = box.index(smallest)
        total += smallest * len(box)
        return adder(box[:pos],total, initial_minimum)

t = int(input())

for _ in range(t):
    n = int(input())
    boxes = input().split()
    for i in range(len(boxes)):
        boxes[i] = int(boxes[i])
    in_min = min(boxes)
    print(adder(boxes,0,in_min))
