src/tools/miri/tests/fail/function_pointers/cast_int_to_fn_ptr.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Validation makes this fail in the wrong place
//@compile-flags: -Zmiri-disable-validation

fn main() {
    let g = unsafe { std::mem::transmute::<usize, fn(i32)>(42) };

    g(42) //~ ERROR: is a dangling pointer
}


