def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    elif len(items) == 2:
        return ' and '.join(items)
    elif len(items) == 3:
        return (', '.join(items[0:2]) + ", and " + (items[2]))
    elif len(items) > 3:
        return (', '.join(items[0:-1]) + ", and " + (items[-1]))
    else:
        print("broken")
