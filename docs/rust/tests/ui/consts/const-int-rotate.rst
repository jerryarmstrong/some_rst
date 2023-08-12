tests/ui/consts/const-int-rotate.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &'static i32 = &(5_i32.rotate_left(3));
    //~^ ERROR temporary value dropped while borrowed
    let y: &'static i32 = &(5_i32.rotate_right(3));
    //~^ ERROR temporary value dropped while borrowed
}


