from quicktest import test


def parens(s):
    stack = []
    count = 0
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                count += 1
            else:
                stack.pop()
    return count + len(stack)


if __name__ == '__main__':
    test(
        parens,
        [
            ('()())()', 1),
            (')(', 2),
            # This next test will cause a failure
            ('()', "2"),
            # This next test will cause an error
            (1, '')
        ]
    )
