tests/ui/enum-discriminant/niche-prefer-zero.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that niche selection prefers zero.
// See https://github.com/rust-lang/rust/pull/87794
// run-pass
#[repr(u8)]
pub enum Size {
    One = 1,
    Two = 2,
    Three = 3,
}

fn main() {
    // check that `None` is zero
    assert_eq!(0, unsafe { std::mem::transmute::<Option<Size>, u8>(None) });
}


