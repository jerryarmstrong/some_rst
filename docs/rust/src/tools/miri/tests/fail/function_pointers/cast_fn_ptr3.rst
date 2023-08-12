src/tools/miri/tests/fail/function_pointers/cast_fn_ptr3.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f(_: (i32, i32)) {}

    let g = unsafe { std::mem::transmute::<fn((i32, i32)), fn()>(f) };

    g() //~ ERROR: calling a function with fewer arguments than it requires
}


