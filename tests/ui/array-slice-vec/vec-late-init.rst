tests/ui/array-slice-vec/vec-late-init.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]


pub fn main() {
    let mut later: Vec<isize> ;
    if true { later = vec![1]; } else { later = vec![2]; }
    println!("{}", later[0]);
}


