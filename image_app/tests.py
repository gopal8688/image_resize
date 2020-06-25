



# reverse the string wiyh out changing the word

s = "I am in bangalore"

# "Bangalore in am I"
print(" ".join(s.split()[::-1]))
"""
1->2->3->4->5 + 1->2->9
"""
l1 = "1->2->3->4->5"
l2 = "1->2->9"
def get_num(link):
    num_list = link.split("->")
    int_val = 0
    for i in num_list:
        int_val = int_val * 10 + int(i)
    return int_val

print(get_num(l1) + get_num(l2))

# celery, syncIO
# rebliMq
# Redis



