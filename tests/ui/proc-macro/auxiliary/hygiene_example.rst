tests/ui/proc-macro/auxiliary/hygiene_example.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate hygiene_example_codegen;

pub use hygiene_example_codegen::hello;

pub fn print(string: &str) {
    println!("{}", string);
}


