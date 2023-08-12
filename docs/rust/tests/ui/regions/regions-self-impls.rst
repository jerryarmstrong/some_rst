tests/ui/regions/regions-self-impls.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

struct Clam<'a> {
    chowder: &'a isize
}

trait get_chowder<'a> {
    fn get_chowder(&self) -> &'a isize;
}

impl<'a> get_chowder<'a> for Clam<'a> {
    fn get_chowder(&self) -> &'a isize { return self.chowder; }
}

pub fn main() {
    let clam = Clam { chowder: &3 };
    println!("{}", *clam.get_chowder());
    clam.get_chowder();
}


