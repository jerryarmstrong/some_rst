tests/ui/binop/binop-mul-i32-f32.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: i32, y: f32) -> f32 {
    x * y //~ ERROR cannot multiply `i32` by `f32`
}

fn main() {}


