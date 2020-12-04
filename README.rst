.. _vardef:
.. role:: python(code)
   :language: python

vardef: contained and organized variable definition
===================================================

`Usage Examples 🚩 <https://vardef.readthedocs.io/en/latest/usage/index.html>`_ | `Developer Reference 👩‍💻 <https://vardef.readthedocs.io/en/latest/reference/index.html>`_ | `Authors 👫 <https://vardef.readthedocs.io/en/latest/authors.html>`_

.. start-badges

.. list-table::
    :stub-columns: 1

    * - license
      - |license|
    * - docs
      - |docs|
    * - tests
      - |build| |dependencies| |coveralls| |reliability| |security| |black| |flake8|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |platforms| |downloads|
.. |docs| image:: https://readthedocs.org/projects/pip/badge/?version=latest&style=plastic
    :target: https://vardef.readthedocs.io/en/latest/
    :alt: Documentation

.. |build| image:: https://github.com/allrod5/vardef/workflows/build/badge.svg
    :alt: Build Status
    :target: https://github.com/allrod5/vardef/actions

.. |dependencies| image:: https://img.shields.io/badge/dependencies-none-brightgreen.svg
    :alt: Dependencies: None
    :target: https://github.com/allrod5/vardef/blob/master/setup.py#L48

.. |coveralls| image:: https://coveralls.io/repos/allrod5/vardef/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/allrod5/vardef

.. |reliability| image:: https://sonarcloud.io/api/project_badges/measure?project=allrod5_vardef&metric=reliability_rating
    :alt: Reliability Rating
    :target: https://sonarcloud.io/dashboard?id=allrod5_vardef

.. |security| image:: https://sonarcloud.io/api/project_badges/measure?project=allrod5_vardef&metric=security_rating
    :alt: Security Rating
    :target: https://sonarcloud.io/dashboard?id=allrod5_vardef

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code Style
    :target: https://github.com/psf/black

.. |flake8| image:: https://img.shields.io/badge/standards-flake8-blue
    :alt: Standards
    :target: https://flake8.pycqa.org/en/latest/

.. |version| image:: https://img.shields.io/pypi/v/vardef.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/vardef

.. |wheel| image:: https://img.shields.io/pypi/wheel/vardef.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/vardef

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/vardef.svg
    :alt: Supported versions
    :target: https://pypi.org/project/vardef

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/vardef.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/vardef

.. |license| image:: https://img.shields.io/github/license/allrod5/vardef
    :alt: GitHub license
    :target: https://github.com/allrod5/vardef/blob/master/LICENSE

.. |platforms| image:: https://img.shields.io/badge/platforms-windows%20%7C%20macos%20%7C%20linux-lightgrey
    :alt: Supported Platforms
    :target: https://github.com/allrod5/vardef/blob/master/.github/workflows/build.yml#L11

.. |downloads| image:: https://pepy.tech/badge/vardef/month
    :alt: Downloads per Month
    :target: https://pepy.tech/project/vardef


.. end-badges

**vardef** is a simple idea for declaring variables in multiple statements in a contained
and organized fashion.

*A simple Python decorator built with Heart and designed for Humans*

.. list-table::
    :header-rows: 0

    * - .. code:: python

            from vardef import vardef


            vars_defined = 0

            @vardef
            def somevar() -> int:
                global vars_defined
                vars_defined += 1
                return 42

            @vardef
            def othervar() -> int:
                global vars_defined
                vars_defined += 1
                return 73

            print(vars_defined)
            # 2

            print(somevar)
            # 42

            print(othervar)
            # 73

            print(type(somevar))
            # <class 'int'>

            print(type(othervar))
            # <class 'int'>

        .. code:: python

            from unittest.mock import Mock
            from vardef import vardef

            from somewhere import User


            @vardef
            def user_with_read_role() -> Mock:
                user_mock = Mock(User)
                user_mock.roles = ["READ"]
                return user_mock

            print(user_with_read_role.roles)
            # ['READ']

            print(type(user_with_read_role))
            # <class 'unittest.mock.Mock'>

      - .. code:: python

            import pandas as pd

            from butterfree.extract import Source
            from butterfree.extract.readers import TableReader
            from butterfree.clients import SparkClient
            from vardef import vardef


            spark_client = SparkClient()

            @vardef
            def df() -> pd.DataFrame:
                source = Source(
                    readers=[TableReader(
                        id="colors",
                        database="datalake_colors",
                        table="colors",
                    )],
                    query="""
                        SELECT * FROM colors
                    """,
                )
                return source.construct(spark_client)

            df.createOrReplaceTempView("colors")
            ...

        .. code:: python

            from vardef import vardef


            @vardef
            def buggy() -> int:
                return 4 / 0

            # Traceback (most recent call last):
            #   File "./buggy.py", line 5, in <module>
            #     def buggy() -> int:
            #   File "./vardef/__init__.py", line 7, in vardef
            #     return define_var()
            #   File "./buggy.py", line 6, in buggy
            #     return 4 / 0
            # ZeroDivisionError: division by zero


Why to use vardef
-----------------

* **Organization**: using a *vardef* function allows all necessary code to define and
  initialize a variable to be logically separated from the outer scope. This makes it
  clear what code is relevant to the rest of the scope and what code is only there to
  assist with initialization. Also, in this way, auxiliary code is avoided being exposed
  to be imported or messed up by external agents.

* **Conciseness**: a *vardef* function is a syntax sugar to avoid the need to declare
  a function which will only be called once to define a variable. With the decorator
  your code gets concise and also avoids exposing the initializer function.

For further information on how to use the decorator check out our `docs
<https://vardef.readthedocs.io/en/latest/>`_!
