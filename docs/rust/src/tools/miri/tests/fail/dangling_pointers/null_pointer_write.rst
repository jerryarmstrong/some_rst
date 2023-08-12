src/tools/miri/tests/fail/dangling_pointers/null_pointer_write.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(deref_nullptr)]
fn main() {
    unsafe { *std::ptr::null_mut() = 0i32 }; //~ ERROR: null pointer is a dangling pointer
}


