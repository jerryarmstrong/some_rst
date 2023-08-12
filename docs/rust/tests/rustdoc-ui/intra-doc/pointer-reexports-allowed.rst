tests/rustdoc-ui/intra-doc/pointer-reexports-allowed.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:pointer-reexports-allowed.rs
// check-pass
extern crate inner;
pub use inner::foo;


