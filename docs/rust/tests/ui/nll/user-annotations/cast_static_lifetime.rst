tests/ui/nll/user-annotations/cast_static_lifetime.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]

fn main() {
    let x = 22_u32;
    let y: &u32 = (&x) as &'static u32; //~ ERROR `x` does not live long enough
}


