src/tools/miri/tests/fail/rc_as_ptr.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail even without validation
//@compile-flags: -Zmiri-disable-validation

use std::ptr;
use std::rc::{Rc, Weak};

/// Taken from the `Weak::as_ptr` doctest.
fn main() {
    let strong = Rc::new(Box::new(42));
    let weak = Rc::downgrade(&strong);
    // Both point to the same object
    assert!(ptr::eq(&*strong, Weak::as_ptr(&weak)));
    // The strong here keeps it alive, so we can still access the object.
    assert_eq!(42, **unsafe { &*Weak::as_ptr(&weak) });

    drop(strong);
    // But not any more. We can do Weak::as_raw(&weak), but accessing the pointer would lead to
    // undefined behaviour.
    assert_eq!(42, **unsafe { &*Weak::as_ptr(&weak) }); //~ ERROR: dereferenced after this allocation got freed
}


