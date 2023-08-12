tests/ui/async-await/issue-67765-async-diagnostic.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
//
// Regression test for issue #67765
// Tests that we point at the proper location when giving
// a lifetime error.
fn main() {}

async fn func<'a>() -> Result<(), &'a str> {
    let s = String::new();

    let b = &s[..];

    Err(b)?; //~ ERROR cannot return value referencing local variable `s`

    Ok(())
}


