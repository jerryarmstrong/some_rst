src/tools/clippy/tests/workspace_test/build.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::print_stdout)]

fn main() {
    // Test for #6041
    println!("Hello");
    print!("Hello");
}


