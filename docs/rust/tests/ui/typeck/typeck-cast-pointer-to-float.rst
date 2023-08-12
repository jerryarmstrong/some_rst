tests/ui/typeck/typeck-cast-pointer-to-float.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x : i16 = 22;
    ((&x) as *const i16) as f32;
    //~^ ERROR casting `*const i16` as `f32` is invalid
}


