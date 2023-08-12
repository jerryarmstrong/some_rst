tests/ui/privacy/private-item-simple.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    fn f() {}
}

fn main() {
    a::f(); //~ ERROR function `f` is private
}


