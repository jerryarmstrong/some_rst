tests/ui/order-dependent-cast-inference.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // Tests case where inference fails due to the order in which casts are checked.
    // Ideally this would compile, see #48270.
    let x = &"hello";
    let mut y = 0 as *const _;
    //~^ ERROR cannot cast to a pointer of an unknown kind
    y = x as *const _;
}


