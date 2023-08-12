src/tools/clippy/tests/ui/auxiliary/non-exhaustive-enum.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Stripped down version of the ErrorKind enum of std
#[non_exhaustive]
pub enum ErrorKind {
    NotFound,
    PermissionDenied,
    #[doc(hidden)]
    Uncategorized,
}


