src/tools/miri/tests/fail/function_pointers/execute_memory.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Validation makes this fail in the wrong place
//@compile-flags: -Zmiri-disable-validation

#![feature(box_syntax)]

fn main() {
    let x = box 42;
    unsafe {
        let f = std::mem::transmute::<Box<i32>, fn()>(x);
        f() //~ ERROR: function pointer but it does not point to a function
    }
}


