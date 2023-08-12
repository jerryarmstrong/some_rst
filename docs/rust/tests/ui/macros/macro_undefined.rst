tests/ui/macros/macro_undefined.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test macro_undefined issue

mod m {
    #[macro_export]
    macro_rules! kl {
        () => ()
    }
}

fn main() {
    k!(); //~ ERROR cannot find
    kl!();
}


