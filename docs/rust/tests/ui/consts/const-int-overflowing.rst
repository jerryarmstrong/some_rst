tests/ui/consts/const-int-overflowing.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &'static (i32, bool) = &(5_i32.overflowing_add(3));
    //~^ ERROR temporary value dropped while borrowed
    let y: &'static (i32, bool) = &(5_i32.overflowing_sub(3));
    //~^ ERROR temporary value dropped while borrowed
    let z: &'static (i32, bool) = &(5_i32.overflowing_mul(3));
    //~^ ERROR temporary value dropped while borrowed
}


