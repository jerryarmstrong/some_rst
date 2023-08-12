tests/ui/for-loop-while/for-loop-panic.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


pub fn main() { let x: Vec<isize> = Vec::new(); for _ in &x { panic!("moop"); } }


