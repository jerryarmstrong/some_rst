tests/run-make-fulldeps/issue-22131/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// ```rust
/// assert_eq!(foo::foo(), 1);
/// ```
#[cfg(feature = "bar")]
pub fn foo() -> i32 { 1 }


