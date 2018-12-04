import quicktest


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
    quicktest.test(
        parens,
        [
            ('()())()', 1),
            (')(', 2),
            # This next test is clearly erroneous and is meant to show how failures are printed
            ('()', "2")
        ]
    )
