from vardef import vardef


class Bar:
    counter = 0


@vardef
def bar() -> int:
    Bar.counter += 1
    return Bar.counter
