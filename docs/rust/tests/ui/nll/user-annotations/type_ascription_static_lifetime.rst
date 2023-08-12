tests/ui/nll/user-annotations/type_ascription_static_lifetime.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]
#![feature(type_ascription)]

fn main() {
    let x = 22_u32;
    let y: &u32 = type_ascribe!(&x, &'static u32); //~ ERROR E0597
}


