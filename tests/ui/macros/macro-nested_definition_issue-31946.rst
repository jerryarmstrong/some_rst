tests/ui/macros/macro-nested_definition_issue-31946.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn main() {
    println!("{}", {
        macro_rules! foo {
            ($name:expr) => { concat!("hello ", $name) }
        }
        foo!("rust")
    });
}


