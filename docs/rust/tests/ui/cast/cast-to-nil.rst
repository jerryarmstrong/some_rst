tests/ui/cast/cast-to-nil.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: non-primitive cast: `u32` as `()`
fn main() { let u = 0u32 as (); }


