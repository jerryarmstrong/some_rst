src/tools/miri/tests/pass/hide_stdout.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-mute-stdout-stderr

fn main() {
    println!("print to stdout");
    eprintln!("print to stderr");
}


