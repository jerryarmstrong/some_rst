tests/ui/attributes/suffixed-literal-meta.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_dummy = 1usize] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1u8] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1u16] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1u32] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1u64] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1isize] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1i8] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1i16] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1i32] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1i64] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1.0f32] //~ ERROR: suffixed literals are not allowed in attributes
#[rustc_dummy = 1.0f64] //~ ERROR: suffixed literals are not allowed in attributes
fn main() {}


