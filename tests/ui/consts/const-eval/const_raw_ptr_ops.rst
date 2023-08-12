tests/ui/consts/const-eval/const_raw_ptr_ops.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

// unconst and bad, will thus error in miri
const X: bool = unsafe { &1 as *const i32 == &2 as *const i32 }; //~ ERROR can't compare
// unconst and bad, will thus error in miri
const X2: bool = unsafe { 42 as *const i32 == 43 as *const i32 }; //~ ERROR can't compare


