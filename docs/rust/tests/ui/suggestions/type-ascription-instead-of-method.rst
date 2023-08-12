tests/ui/suggestions/type-ascription-instead-of-method.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    let _ = Box:new("foo".to_string());
    //~^ ERROR expected type, found
}


