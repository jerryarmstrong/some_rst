src/tools/clippy/tests/ui/builtin_type_shadow.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::builtin_type_shadow)]
#![allow(non_camel_case_types)]

fn foo<u32>(a: u32) -> u32 {
    42
    // ^ rustc's type error
}

fn main() {}


