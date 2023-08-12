tests/ui/consts/const-int-sign.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &'static bool = &(5_i32.is_negative());
    //~^ ERROR temporary value dropped while borrowed
    let y: &'static bool = &(5_i32.is_positive());
    //~^ ERROR temporary value dropped while borrowed
}


