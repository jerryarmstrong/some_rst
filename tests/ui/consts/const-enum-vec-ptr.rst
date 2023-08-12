tests/ui/consts/const-enum-vec-ptr.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

enum E { V1(isize), V0 }
static C: &'static [E] = &[E::V0, E::V1(0xDEADBEE), E::V0];

pub fn main() {
    match C[1] {
        E::V1(n) => assert_eq!(n, 0xDEADBEE),
        _ => panic!()
    }
    match C[2] {
        E::V0 => (),
        _ => panic!()
    }
}


