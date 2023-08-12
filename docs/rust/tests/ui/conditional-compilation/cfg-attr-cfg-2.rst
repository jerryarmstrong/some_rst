tests/ui/conditional-compilation/cfg-attr-cfg-2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //
// error-pattern: `main` function not found
// compile-flags: --cfg foo

// main is conditionally compiled, but the conditional compilation
// is conditional too!

#[cfg_attr(foo, cfg(bar))]
fn main() { }


