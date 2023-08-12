tests/ui/consts/min_const_fn/address_of_const.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(raw_ref_op)]

const fn const_address_of_in_const() {
    let mut a = 0;
    let b = &raw const a;
}

struct X;

impl X {
    const fn inherent_const_address_of_in_const() {
        let mut a = 0;
        let b = &raw const a;
    }
}

fn main() {}


