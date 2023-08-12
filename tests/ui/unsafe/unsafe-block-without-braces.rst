tests/ui/unsafe/unsafe-block-without-braces.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    unsafe //{
        std::mem::transmute::<f32, u32>(1.0);
    //}
}
//~^^^ ERROR expected `{`, found `std`


