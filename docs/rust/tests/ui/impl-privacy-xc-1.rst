tests/ui/impl-privacy-xc-1.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:impl_privacy_xc_1.rs

// pretty-expanded FIXME #23616

extern crate impl_privacy_xc_1;

pub fn main() {
    let fish = impl_privacy_xc_1::Fish { x: 1 };
    fish.swim();
}


