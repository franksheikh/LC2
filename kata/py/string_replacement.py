def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    if n == 1:
        return "%s likes this" % names[0]
    if n == 2:
        return "%s and %s like this" % (names[0], names[1])
    if n == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %d others like this" % (names[0], names[1], n - 2)