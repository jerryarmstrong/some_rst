tests/rustdoc-ui/error-in-impl-trait/impl-keyword.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
pub trait ValidTrait {}
/// This returns impl trait
pub fn g() -> impl ValidTrait {
    error::_in::impl_trait()
}


