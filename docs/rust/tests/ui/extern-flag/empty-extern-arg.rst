tests/ui/extern-flag/empty-extern-arg.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --extern std=
// error-pattern: extern location for std does not exist
// needs-unwind since it affects the error output
// ignore-emscripten missing eh_catch_typeinfo lang item

fn main() {}


