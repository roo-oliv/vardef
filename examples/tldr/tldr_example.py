"""
This is an straightforward example of the vardef decorator.

.. seealso::

    For better understanding of this decorator you can look at the other examples in
    the :ref:`usage_examples` section. The :ref:`basic_usage_example` is a good start!
"""
# sphinx-start
from vardef import vardef


def run_example():
    @vardef
    def foo() -> int:
        return 42

    print(foo)
    # 42

    print(type(foo))
    # <class 'int'>


if __name__ == "__main__":
    run_example()
