src/tools/miri/tests/fail/alloc/stack_free.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Validation/SB changes why we fail
//@compile-flags: -Zmiri-disable-validation -Zmiri-disable-stacked-borrows

//@error-pattern: /deallocating .*, which is stack variable memory, using Rust heap deallocation operation/

fn main() {
    let x = 42;
    let bad_box = unsafe { std::mem::transmute::<&i32, Box<i32>>(&x) };
    drop(bad_box);
}


