tests/ui/impl-trait/auto-trait-leak.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::Cell;
use std::rc::Rc;

fn send<T: Send>(_: T) {}

fn main() {
}

// Cycles should work as the deferred obligations are
// independently resolved and only require the concrete
// return type, which can't depend on the obligation.
fn cycle1() -> impl Clone {
    //~^ ERROR cycle detected
    send(cycle2().clone());

    Rc::new(Cell::new(5))
}

fn cycle2() -> impl Clone {
    send(cycle1().clone());

    Rc::new(String::from("foo"))
}


