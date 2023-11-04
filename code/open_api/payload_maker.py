map = {
    "/root": "obj",
    "/root/a": "obj",
    "/root/a/b": "obj",
    "/root/a/b/c": "str",
    "/root/a/b/d": "str"
}

f = open("in.txt")

d = {}


def foo(parent, child, xpath):
    if type(parent) is dict:
        if map[xpath] == "obj":
            if child not in parent:
                parent[child] = {}
        if map[xpath] == "str":
            parent[child] = "sample"
    return parent[child]
    # return child


# parent = None
# for line in f:
#     x = line.strip().split('/')
#     for child in x:
#         parent = foo(parent, child)
# f.close()


def sak():
    x = ["root", "a", "b", "c"]
    temp = d
    q = ''
    for child in x:
        q = q + '/' + child
        temp = foo(temp, child, q)
    print(d)




if __name__ == '__main__':
    sak()
