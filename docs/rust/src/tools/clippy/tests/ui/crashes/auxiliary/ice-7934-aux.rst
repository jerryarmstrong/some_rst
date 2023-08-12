src/tools/clippy/tests/ui/crashes/auxiliary/ice-7934-aux.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn zero() {
    // SAFETY:
    unsafe { 0 };
}


