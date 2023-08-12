tests/ui/binding/pat-tuple-7.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    #[allow(unused_parens)]
    match 0 {
        (pat) => assert_eq!(pat, 0)
    }
}


