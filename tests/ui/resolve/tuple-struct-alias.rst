tests/ui/resolve/tuple-struct-alias.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S(u8, u16);
type A = S;

fn main() {
    let s = A(0, 1); //~ ERROR expected function
    match s {
        A(..) => {} //~ ERROR expected tuple struct or tuple variant
    }
}


