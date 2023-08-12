src/tools/miri/tests/fail/function_pointers/cast_fn_ptr1.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f() {}

    let g = unsafe { std::mem::transmute::<fn(), fn(i32)>(f) };

    g(42) //~ ERROR: calling a function with more arguments than it expected
}


