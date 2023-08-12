src/tools/miri/tests/fail/intrinsics/zero_fn_ptr.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(deprecated, invalid_value)]
fn main() {
    unsafe { std::mem::zeroed::<fn()>() };
    //~^ ERROR: attempted to zero-initialize type `fn()`, which is invalid
}


