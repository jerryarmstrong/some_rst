src/tools/miri/tests/fail/function_pointers/cast_box_int_to_fn_ptr.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Validation makes this fail in the wrong place
//@compile-flags: -Zmiri-disable-validation

fn main() {
    let b = Box::new(42);
    let g = unsafe { std::mem::transmute::<&Box<usize>, &fn(i32)>(&b) };

    (*g)(42) //~ ERROR: it does not point to a function
}


