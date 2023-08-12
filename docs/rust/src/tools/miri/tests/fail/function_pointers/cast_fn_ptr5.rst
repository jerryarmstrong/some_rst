src/tools/miri/tests/fail/function_pointers/cast_fn_ptr5.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f() -> u32 {
        42
    }

    let g = unsafe { std::mem::transmute::<fn() -> u32, fn()>(f) };

    g() //~ ERROR: calling a function with return type u32 passing return place of type ()
}


