tests/ui/does-nothing.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() { println!("doing"); this_does_nothing_what_the; println!("boing"); }
//~^ ERROR cannot find value `this_does_nothing_what_the` in this scope


