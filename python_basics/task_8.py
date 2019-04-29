# Task: https://stepik.org/lesson/24462/step/7?unit=6768

# import sys
# sys.stdin = open("input.txt", "r")

classes = {}


def add(class_name, ancestors):
    classes[class_name] = ancestors


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
for i in range(0, n):
    supposed_ancestors, class_name = input().split()
    # print(f'is_ans({supposed_ancestors}, {class_name})')
    if is_ancestor(supposed_ancestors, class_name):
        print('Yes')
    else:
        print('No')
# print('end')
