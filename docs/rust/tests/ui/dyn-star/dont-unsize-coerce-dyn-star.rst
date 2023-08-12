tests/ui/dyn-star/dont-unsize-coerce-dyn-star.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// check-run-results

#![feature(dyn_star)]
//~^ WARN the feature `dyn_star` is incomplete and may not be safe to use and/or cause compiler crashes

trait AddOne {
    fn add1(&mut self) -> usize;
}

impl AddOne for usize {
    fn add1(&mut self) -> usize {
        *self += 1;
        *self
    }
}

fn add_one(i: &mut (dyn* AddOne + '_)) -> usize {
    i.add1()
}

fn main() {
    let mut x = 42usize as dyn* AddOne;

    println!("{}", add_one(&mut x));
    println!("{}", add_one(&mut x));
}


