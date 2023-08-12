src/tools/miri/tests/fail/function_pointers/cast_fn_ptr4.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f(_: *const [i32]) {}

    let g = unsafe { std::mem::transmute::<fn(*const [i32]), fn(*const i32)>(f) };

    g(&42 as *const i32) //~ ERROR: calling a function with argument of type *const [i32] passing data of type *const i32
}


