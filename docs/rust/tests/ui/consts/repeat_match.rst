tests/ui/consts/repeat_match.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// https://github.com/rust-lang/rust/issues/45044

const X: [u8; 1] = [0; 1];

fn main() {
    match &X {
        &X => println!("a"),
        _ => println!("b"),
    };
}


