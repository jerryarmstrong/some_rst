tests/ui/cast/cast-to-infer-ty.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Check that we allow a cast to `_` so long as the target type can be
// inferred elsewhere.

pub fn main() {
    let i: *const i32 = 0 as _;
    assert!(i.is_null());
}


