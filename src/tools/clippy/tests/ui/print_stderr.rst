src/tools/clippy/tests/ui/print_stderr.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::print_stderr)]

fn main() {
    eprintln!("Hello");
    println!("This should not do anything");
    eprint!("World");
    print!("Nor should this");
}


