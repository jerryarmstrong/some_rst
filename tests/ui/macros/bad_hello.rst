tests/ui/macros/bad_hello.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!(3 + 4);
    //~^ ERROR format argument must be a string literal
    println!(3, 4);
    //~^ ERROR format argument must be a string literal
}


