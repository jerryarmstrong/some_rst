tests/run-make/native-link-modifier-whole-archive/directly_linked.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::io::Write;

fn main() {
    print!("directly_linked.");
    std::io::stdout().flush().unwrap();
}


