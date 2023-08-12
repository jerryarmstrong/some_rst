tests/ui/conditional-compilation/cfg-attr-invalid-predicate.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(foo(bar))] //~ ERROR invalid predicate `foo`
fn check() {}

fn main() {}


