tests/ui/imports/import-crate-with-invalid-spans/auxiliary/crate_with_invalid_spans_macros.rs
=============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! add1 {
    ($e:expr) => ({
        let a = 1 + $e;
        let b = $e + 1;
        a + b - 1
    })
}


