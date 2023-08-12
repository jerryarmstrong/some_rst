tests/ui/binding/match-unsized.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn main() {
    let data: &'static str = "Hello, World!";
    match data {
        &ref xs => {
            assert_eq!(data, xs);
        }
    }
}


