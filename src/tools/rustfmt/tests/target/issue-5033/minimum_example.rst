src/tools/rustfmt/tests/target/issue-5033/minimum_example.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // leading comment

#![rustfmt::skip]
fn main() {
    println!("main"); // commented
}

// post comment


