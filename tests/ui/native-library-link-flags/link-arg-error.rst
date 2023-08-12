tests/ui/native-library-link-flags/link-arg-error.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -l link-arg:+bundle=arg -Z unstable-options
// error-pattern: linking modifier `bundle` is only compatible with `static` linking kind

fn main() {}


