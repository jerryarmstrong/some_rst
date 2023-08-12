tests/ui/consts/min_const_fn/mutable_borrow.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const fn mutable_ref_in_const() -> u8 {
    let mut a = 0;
    let b = &mut a; //~ ERROR mutable references
    *b
}

struct X;

impl X {
    const fn inherent_mutable_ref_in_const() -> u8 {
        let mut a = 0;
        let b = &mut a; //~ ERROR mutable references
        *b
    }
}

fn main() {}


