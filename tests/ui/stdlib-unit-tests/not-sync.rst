tests/ui/stdlib-unit-tests/not-sync.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::{Cell, RefCell};
use std::rc::{Rc, Weak};
use std::sync::mpsc::{Receiver, Sender};

fn test<T: Sync>() {}

fn main() {
    test::<Cell<i32>>();
    //~^ ERROR `Cell<i32>` cannot be shared between threads safely [E0277]
    test::<RefCell<i32>>();
    //~^ ERROR `RefCell<i32>` cannot be shared between threads safely [E0277]

    test::<Rc<i32>>();
    //~^ ERROR `Rc<i32>` cannot be shared between threads safely [E0277]
    test::<Weak<i32>>();
    //~^ ERROR `std::rc::Weak<i32>` cannot be shared between threads safely [E0277]

    test::<Receiver<i32>>();
    //~^ ERROR `std::sync::mpsc::Receiver<i32>` cannot be shared between threads safely [E0277]
    test::<Sender<i32>>();
    //~^ ERROR `Sender<i32>` cannot be shared between threads safely [E0277]
}


