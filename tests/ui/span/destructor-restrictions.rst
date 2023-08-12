tests/ui/span/destructor-restrictions.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests the new destructor semantics.

use std::cell::RefCell;

fn main() {
    let b = {
        let a = Box::new(RefCell::new(4));
        *a.borrow() + 1
    }; //~^ ERROR `*a` does not live long enough
    println!("{}", b);
}


