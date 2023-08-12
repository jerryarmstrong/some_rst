tests/run-make-fulldeps/issue-64153/upstream.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make this function extern "C", public, and no-mangle, so that it gets
// exported from the downstream staticlib.
#[no_mangle]
pub extern "C" fn issue64153_test_function(x: u32) -> u32 {
    x + 1
}


