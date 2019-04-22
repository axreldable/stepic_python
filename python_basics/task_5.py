# create <namespace> <parent>
# add <namespace> <var>
# get <namespace> <var>


main_dict = {
    'global': {
        'parent': None,
        'vars': set('a'),
        'foo': {
            'parent': 'global',
            'vars': set('b'),
            'bar': {
                'parent': 'foo',
                'vars': set('a')}
        }
    }
}

dict1 = {
    'global': {
        'parent': None,
        'vars': set()
    }
}

cur_dict = dict1['global']


def create(namespace, parent):
    create_d(dict1, namespace, parent)


def create_d(dic, namespace, parent):
    if dic[parent][namespace] is None:
        dic[parent][namespace] = {
            'parent': parent,
            'vars': set()
        }
    else:
        for key in dic.keys():
            create_d(dic[key], namespace, parent)


def add(namespace, var):
    cur_dict[namespace]['vars'].add(var)


# def get(namespace, var):
#     return cur_dict[name]

print(cur_dict)
create('foo', 'global')
print(cur_dict)
add('foo', 'a')
print(cur_dict)
create('bar', 'foo')
print(cur_dict)

