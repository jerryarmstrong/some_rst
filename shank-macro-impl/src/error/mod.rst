shank-macro-impl/src/error/mod.rs
=================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    mod program_error;
mod this_error;

pub use program_error::*;
pub use this_error::*;

pub const DERIVE_THIS_ERROR_ATTR: &str = "Error";


