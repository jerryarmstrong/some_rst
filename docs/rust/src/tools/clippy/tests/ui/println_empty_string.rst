src/tools/clippy/tests/ui/println_empty_string.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(clippy::match_single_binding)]

fn main() {
    println!();
    println!("");

    match "a" {
        _ => println!(""),
    }

    eprintln!();
    eprintln!("");

    match "a" {
        _ => eprintln!(""),
    }
}


