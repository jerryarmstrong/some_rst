tests/ui/suggestions/suggest-remove-refs-5.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    let v = &mut &mut Vec::<i32>::new();
    for _ in &mut &mut v {} //~ ERROR E0277

    let v = &mut &mut [1u8];
    for _ in &mut v {} //~ ERROR E0277
}


