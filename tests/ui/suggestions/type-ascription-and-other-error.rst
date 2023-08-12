tests/ui/suggestions/type-ascription-and-other-error.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    not rust; //~ ERROR
    let _ = 0: i32; // (error hidden by existing error)
    #[cfg(FALSE)]
    let _ = 0: i32; // (warning hidden by existing error)
}


