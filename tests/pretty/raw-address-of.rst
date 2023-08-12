tests/pretty/raw-address-of.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact
#![feature(raw_ref_op)]

const C_PTR: () = { let a = 1; &raw const a; };
static S_PTR: () = { let b = false; &raw const b; };

fn main() {
    let x = 123;
    let mut y = 345;
    let c_p = &raw const x;
    let parens = unsafe { *(&raw mut (y)) };
}


