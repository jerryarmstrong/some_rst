tests/ui/span/suggestion-non-ascii.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let tup = (1,);
    println!("☃{}", tup[0]); //~ ERROR cannot index into a value of type
}


