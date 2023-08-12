tests/rustdoc-ui/error-in-impl-trait/generic-argument.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
trait ValidTrait {}

/// This has docs
pub fn f() -> impl ValidTrait {
    Vec::<DoesNotExist>::new()
}


