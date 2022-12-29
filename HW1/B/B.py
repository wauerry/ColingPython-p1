penguin1 = '   _~_   '
penguin2 = '  (o o)  '
penguin3 = ' /  V  \\ '
penguin4 = '/(  _  )\\'
penguin5 = '  ^^ ^^  '


def solution(n):
    if n == 0:
        return ''
    return penguin1 * n + '\n' + penguin2 * n + '\n' + penguin3 * n + '\n' + penguin4 * n + '\n' + penguin5 * n
