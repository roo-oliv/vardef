"""
In this example you'll get to know how it is to use vardef.

We will declare a variable `secret_key` in the `example_utils` module by using the
:meth:`@vardef <vardef.vardef>` decorator. In there we simulate the creation of a
server connection to retrieve the secret and we put the `conn` variable inside the
*vardef* function since we only need it to initialize our variable and do not want
it exposed outside of that scope.

.. seealso::

    The :ref:`other_decorators_interaction_example` shows how to use the
    :meth:`@vardef <vardef.vardef>` decorator alongside other decorators.
"""
# sphinx-start


def run_example():
    from examples.basic_usage.example_utils import secret_key

    # 'secret_key' variable definition started
    # 'secret_key' variable definition finished

    print(secret_key)
    # MySecret

    try:
        from examples.basic_usage.example_utils import conn

        print(f"'conn' exposed: {conn}")
    except ImportError:
        print("'conn' is not exposed")
    # 'conn' is not exposed


if __name__ == "__main__":
    run_example()
