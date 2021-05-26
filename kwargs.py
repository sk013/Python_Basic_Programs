def reverse(l, **kwargs):
    if kwargs.get("reverse_str") == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


l = ['shailander','kumar']
print(reverse(l, reverse_str = True))