tests/ui/suggestions/shadowed-lplace-method.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(unused_imports)]
use std::borrow::BorrowMut;
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    let rc = Rc::new(RefCell::new(true));
    *rc.borrow_mut() = false; //~ ERROR E0308
}


