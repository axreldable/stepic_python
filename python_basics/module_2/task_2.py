# Task: https://stepik.org/lesson/24463/step/7?auth=registration&unit=6771

import sys
sys.stdin = open("input.txt", "r")

classes = {}


def add(class_name, ancestor):
    classes[class_name] = ancestor


def is_ancestor(ancestor, class_name):
    if ancestor == class_name:
        return True
    # if class_name not in classes.keys():
    #     return False
    ancs = classes[class_name]
    if ancs is None:
        return False
    elif ancestor in ancs:
        return True
    else:
        for a in ancs:
            if is_ancestor(ancestor, a):
                return True
        return False


# print('start')
n = int(input())
for i in range(0, n):
    inp = input()
    if ':' in inp:
        class_name, ancestors = inp.split(':')
    else:
        class_name, ancestors = inp, None
    if ancestors is not None:
        ancestors = ancestors.strip().split()
    add(class_name.strip(), ancestors)

# print(classes)

n = int(input())
prev = []
for i in range(0, n):
    # print(prev)
    class_name = input()
    for supposed_ancestors in prev:
        if is_ancestor(supposed_ancestors, class_name):
            print(class_name)
            break
    prev.append(class_name)
# print('end')
