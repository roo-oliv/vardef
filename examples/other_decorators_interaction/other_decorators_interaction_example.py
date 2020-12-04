"""
In this example you'll learn how the vardef decorator interacts with other decorators.

We will declare the function ``my_var`` as a *vardef* function but we will also use
other two decorators, `arg_provider_decorator` and `other_decorator`, in our *vardef*
function.

Since the :meth:`@vardef <vardef.vardef>` decorator turns our function into a regular,
static variable we must use it as the outermost decorator. All other decorators can
come below it without any interference problems.
"""
# sphinx-start
from examples.other_decorators_interaction.other_decorators import (
    arg_provider_decorator,
    other_decorator,
)
from vardef import vardef


def run_example():
    @vardef
    @arg_provider_decorator
    @other_decorator
    def my_var(provided_arg) -> str:
        print("'my_var' vardef executed")
        return provided_arg

    # arg_provider_decorator wrapper executed
    # other_decorator wrapper executed
    # 'my_var' vardef executed

    print(my_var)
    # PROVIDED_VALUE


if __name__ == "__main__":
    run_example()
