tests/ui/typeck/remove-extra-argument.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// Check that the HELP suggestion is `l(vec![])` instead of `l($crate::vec::Vec::new())`
fn l(_a: Vec<u8>) {}

fn main() {
    l(vec![], vec![])
    //~^ ERROR function takes 1 argument but 2 arguments were supplied
    //~| HELP remove the extra argument
}


