tests/ui/cast/cast-from-nil.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: non-primitive cast: `()` as `u32`
fn main() { let u = (assert!(true) as u32); }


