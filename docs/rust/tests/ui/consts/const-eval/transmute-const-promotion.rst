tests/ui/consts/const-eval/transmute-const-promotion.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem;

fn main() {
    let x: &'static u32 = unsafe { &mem::transmute(3.0f32) };
    //~^ ERROR temporary value dropped while borrowed
}


