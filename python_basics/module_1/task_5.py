# create <namespace> <parent>
# add <namespace> <var>
# get <namespace> <var>


namespaces = {
    'global': {
        'parent': None,
        'vars': set()
    }
}


def create(namespace, parent):
    namespaces[namespace] = {
        'parent': parent,
        'vars': set()
    }


def add(namespace, var):
    namespaces[namespace]['vars'].add(var)


def get(namespace, var):
    if var in namespaces[namespace]['vars']:
        return namespace
    elif namespaces[namespace]['parent'] is None:
        return None
    else:
        return get(namespaces[namespace]['parent'], var)


n = int(input())
for i in range(0, n):
    command, namespace, var = input().split()
    if command == 'create':
        create(namespace, var)
    elif command == 'add':
        add(namespace, var)
    else:
        print(get(namespace, var))
