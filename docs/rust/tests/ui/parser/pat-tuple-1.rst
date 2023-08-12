tests/ui/parser/pat-tuple-1.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match (0, 1) {
        (, ..) => {} //~ ERROR expected pattern, found `,`
    }
}


