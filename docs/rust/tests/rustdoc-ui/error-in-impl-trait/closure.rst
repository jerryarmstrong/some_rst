tests/rustdoc-ui/error-in-impl-trait/closure.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// manually desugared version of an `async fn` (but with a closure instead of a generator)
pub fn a() -> impl Fn() -> u32 {
    || content::doesnt::matter()
}


