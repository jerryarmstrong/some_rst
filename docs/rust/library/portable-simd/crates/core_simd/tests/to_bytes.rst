library/portable-simd/crates/core_simd/tests/to_bytes.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(portable_simd, generic_const_exprs, adt_const_params)]
#![allow(incomplete_features)]
#![cfg(feature = "generic_const_exprs")]

use core_simd::Simd;

#[test]
fn byte_convert() {
    let int = Simd::<u32, 2>::from_array([0xdeadbeef, 0x8badf00d]);
    let bytes = int.to_ne_bytes();
    assert_eq!(int[0].to_ne_bytes(), bytes[..4]);
    assert_eq!(int[1].to_ne_bytes(), bytes[4..]);
    assert_eq!(Simd::<u32, 2>::from_ne_bytes(bytes), int);
}


