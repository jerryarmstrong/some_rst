src/tools/miri/tests/fail/dangling_pointers/null_pointer_deref.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(deref_nullptr)]
fn main() {
    let x: i32 = unsafe { *std::ptr::null() }; //~ ERROR: null pointer is a dangling pointer
    panic!("this should never print: {}", x);
}


