tests/ui/imports/issue-26873-multifile/A/mod.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub mod B;
pub mod C;

pub use self::C::T;


