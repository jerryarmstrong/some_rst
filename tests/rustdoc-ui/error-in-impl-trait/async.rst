tests/rustdoc-ui/error-in-impl-trait/async.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// check-pass

/// Should compile fine
pub async fn a() -> u32 {
    error::_in::async_fn()
}


