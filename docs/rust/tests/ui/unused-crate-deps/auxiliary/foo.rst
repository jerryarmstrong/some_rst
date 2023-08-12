tests/ui/unused-crate-deps/auxiliary/foo.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// aux-crate:bar=bar.rs

pub const FOO: &str = "foo";
pub use bar::BAR;


