tests/ui/invalid/invalid-path-in-const.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f(a: [u8; u32::DOESNOTEXIST]) {}
    //~^ ERROR no associated item named `DOESNOTEXIST` found for type `u32`
}


