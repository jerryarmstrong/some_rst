tests/ui/native-library-link-flags/empty-kind-1.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Unspecified kind should fail with an error

// compile-flags: -l =mylib
// error-pattern: unknown library kind ``, expected one of: static, dylib, framework, link-arg

fn main() {}


