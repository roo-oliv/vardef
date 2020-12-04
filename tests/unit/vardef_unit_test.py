from vardef import vardef


def test_vardef_calls_the_function_to_define_the_variable_value():
    # given
    def foo() -> int:
        return 42

    # when
    foo = vardef(foo)

    # then
    assert foo == 42


def test_vardef_calls_the_function_only_once():
    # given
    counter = 0

    # when
    @vardef
    def foo() -> int:
        nonlocal counter
        counter += 1
        return counter

    # then
    assert counter == 1
    assert foo == counter
    assert foo == 1


def test_vardef_imported_calls_the_function_only_once():
    # given
    def import_and_get_bar() -> int:
        from tests.unit.test_module import bar

        return bar

    from tests.unit.test_module import Bar

    # when
    first_call = import_and_get_bar()
    second_call = import_and_get_bar()
    counter = Bar.counter

    # then
    assert first_call == 1
    assert second_call == 1
    assert counter == 1
