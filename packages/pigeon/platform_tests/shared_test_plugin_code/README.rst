packages/pigeon/platform_tests/shared_test_plugin_code/README.md
================================================================

Last edited: 2023-03-17 07:52:27

Contents:

.. code-block:: md

    This package contains the shared code (generated Pigeon output, example app,
integration tests) for `test_plugin` and `alternate_language_shared_plugin`.

Since those two plugin projects are intended to be identical, and only exist
as separate projects because of the Java/Kotlin and Obj-C/Swift overlap that
prevents combining them, almost all Dart code should be in this package rather
than in the plugins themselves.


