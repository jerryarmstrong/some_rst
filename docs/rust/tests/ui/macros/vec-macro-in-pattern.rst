tests/ui/macros/vec-macro-in-pattern.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is a regression test for #61933
// Verify that the vec![] macro may not be used in patterns
// and that the resulting diagnostic is actually helpful.

fn main() {
    match Some(vec![42]) {
        Some(vec![43]) => {} //~ ERROR arbitrary expressions aren't allowed in patterns
        _ => {}
    }
}


