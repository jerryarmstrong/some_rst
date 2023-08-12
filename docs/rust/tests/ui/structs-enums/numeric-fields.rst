tests/ui/structs-enums/numeric-fields.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct S(u8, u16);

fn main() {
    let s = S{1: 10, 0: 11};
    match s {
        S{0: a, 1: b, ..} => {
            assert_eq!(a, 11);
            assert_eq!(b, 10);
        }
    }
}


