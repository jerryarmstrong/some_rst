tests/ui/enum/enum-to-float-cast-2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that enum-to-float casts are disallowed.

enum E {
    L0 = -1,
    H0 = 1
}

enum F {
    L1 = 1,
    H1 = 0xFFFFFFFFFFFFFFFF
}

pub fn main() {
    let a = E::L0 as f32;  //~ ERROR casting
    let c = F::H1 as f32;  //~ ERROR casting
    assert_eq!(a, -1.0f32);
    assert_eq!(c, -1.0f32);
}


