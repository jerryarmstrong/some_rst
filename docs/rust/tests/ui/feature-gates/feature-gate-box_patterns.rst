tests/ui/feature-gates/feature-gate-box_patterns.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let box x = Box::new('c'); //~ ERROR box pattern syntax is experimental
    println!("x: {}", x);
}


