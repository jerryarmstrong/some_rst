tests/ui/type/type-ascription-instead-of-initializer.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: Vec::with_capacity(10, 20);  //~ ERROR expected type, found `10`
    //~^ ERROR function takes 1 argument
}


