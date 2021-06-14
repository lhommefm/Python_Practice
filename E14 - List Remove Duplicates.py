a = ['jim', 'jim', 'james', 'samej', 'poon']

def no_dup_loop(names):
    no_dup_list = []
    for x in names:
        if x not in no_dup_list:
            no_dup_list.append(x)
    return no_dup_list

def no_dup_set(names):
    return list(set(names))

print(no_dup_loop(a))
print(no_dup_set(a))