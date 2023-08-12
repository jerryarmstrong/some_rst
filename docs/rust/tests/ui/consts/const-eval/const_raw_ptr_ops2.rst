tests/ui/consts/const-eval/const_raw_ptr_ops2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

// fine
const Z: i32 = unsafe { *(&1 as *const i32) };

// bad, will thus error in miri
const Z2: i32 = unsafe { *(42 as *const i32) }; //~ ERROR evaluation of constant value failed
//~| is a dangling pointer
const Z3: i32 = unsafe { *(44 as *const i32) }; //~ ERROR evaluation of constant value failed
//~| is a dangling pointer


