tests/ui/utf8_idents.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
//
#![allow(mixed_script_confusables, non_camel_case_types)]

fn foo<
    'β,
    γ
>() {}

struct X {
    δ: usize
}

pub fn main() {
    let α = 0.00001f64;
}


