tests/ui/consts/raw_pointer_promoted.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub const FOO: &'static *const i32 = &(&0 as _);

fn main() {}


