tests/ui/privacy/impl-privacy-xc-2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:impl_privacy_xc_2.rs

extern crate impl_privacy_xc_2;

pub fn main() {
    let fish1 = impl_privacy_xc_2::Fish { x: 1 };
    let fish2 = impl_privacy_xc_2::Fish { x: 2 };
    if fish1.eq(&fish2) { println!("yes") } else { println!("no") };
}


