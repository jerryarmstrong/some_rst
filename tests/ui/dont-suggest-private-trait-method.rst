tests/ui/dont-suggest-private-trait-method.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct T;

fn main() {
    T::new();
    //~^ ERROR no function or associated item named `new` found
}


