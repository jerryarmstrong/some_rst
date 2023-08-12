tests/ui/parser/macro-braces-dot-question.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

use std::io::Write;

fn main() -> Result<(), std::io::Error> {
    vec! { 1, 2, 3 }.len();
    write! { vec![], "" }?;
    println!{""}
    [0]; // separate statement, not indexing into the result of println.
    Ok(())
}


