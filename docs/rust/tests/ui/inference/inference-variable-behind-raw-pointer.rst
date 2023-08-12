tests/ui/inference/inference-variable-behind-raw-pointer.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// tests that the following code compiles, but produces a future-compatibility warning

fn main() {
    let data = std::ptr::null();
    let _ = &data as *const *const ();
    if data.is_null() {}
    //~^ WARNING type annotations needed
    //~| WARNING this is accepted in the current edition
}


