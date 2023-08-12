tests/ui/sepcomp/auxiliary/sepcomp-extern-lib.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
pub extern "C" fn foo() -> usize {
    1234
}


