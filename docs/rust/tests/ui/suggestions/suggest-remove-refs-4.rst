tests/ui/suggestions/suggest-remove-refs-4.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    let foo = &[1,2,3].iter();
    for _i in &foo {} //~ ERROR E0277
}


