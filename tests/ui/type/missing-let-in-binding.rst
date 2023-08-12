tests/ui/type/missing-let-in-binding.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    let mut _foo: i32 = 1;
    _foo: i32 = 4; //~ ERROR type ascription is experimental
}


