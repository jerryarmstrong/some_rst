src/tools/miri/tests/fail/function_pointers/cast_fn_ptr2.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f(_: (i32, i32)) {}

    let g = unsafe { std::mem::transmute::<fn((i32, i32)), fn(i32)>(f) };

    g(42) //~ ERROR: calling a function with argument of type (i32, i32) passing data of type i32
}


