tests/ui/parser/pat-tuple-2.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    match (0, 1, 2) {
        (pat, ..,) => {}
    }
}


