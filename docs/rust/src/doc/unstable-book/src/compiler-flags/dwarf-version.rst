src/doc/unstable-book/src/compiler-flags/dwarf-version.md
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    ## `dwarf-version`

This option controls the version of DWARF that the compiler emits, on platforms
that use DWARF to encode debug information. It takes one of the following
values:

* `2`: DWARF version 2 (the default on certain platforms, like macOS).
* `4`: DWARF version 4 (the default on certain platforms, like Linux).
* `5`: DWARF version 5.


