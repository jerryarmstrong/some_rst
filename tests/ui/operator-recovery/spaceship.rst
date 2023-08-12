tests/ui/operator-recovery/spaceship.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!("{}", 1 <=> 2);
    //~^ERROR invalid comparison operator `<=>`
}


