tests/ui/dyn-star/dyn-star-to-dyn.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

#![feature(dyn_star)]
//~^ WARN the feature `dyn_star` is incomplete and may not be safe to use and/or cause compiler crashes

fn main() {
    let x: dyn* Send = &();
    let x = Box::new(x) as Box<dyn Send>;
}


