# create <namespace> <parent>
# add <namespace> <var>
# get <namespace> <var>

main_dict = {
    "global": {
        "foo": {
            "vars": {
                "a": 1,
                "b": 1,
            }
        },
        "bar": {
            "vars": {
                "a": 1,
                "b": 1,
            }
        },
    }
}

def crate(namespace, parent):
    for  main_dict["global"].keys()


def get_namespace(cur_dict, name):
    return cur_dict[name]