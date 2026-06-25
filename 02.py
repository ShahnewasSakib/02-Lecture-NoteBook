def add_vec(a,b):
    add = a;
    for i in range(len(a)):
        add[i] = a[i] - b[i];
    return add;
Add = add_vec([2,3,5], [3,2,1])
print(Add)