tests/ui/const-generics/slice-const-param.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(adt_const_params)]
#![allow(incomplete_features)]

pub fn function_with_str<const STRING: &'static str>() -> &'static str {
    STRING
}

pub fn function_with_bytes<const BYTES: &'static [u8]>() -> &'static [u8] {
    BYTES
}

pub fn main() {
    assert_eq!(function_with_str::<"Rust">(), "Rust");
    assert_eq!(function_with_str::<"ℇ㇈↦">(), "ℇ㇈↦");
    assert_eq!(function_with_bytes::<b"AAAA">(), &[0x41, 0x41, 0x41, 0x41]);
    assert_eq!(function_with_bytes::<{&[0x41, 0x41, 0x41, 0x41]}>(), b"AAAA");
}


