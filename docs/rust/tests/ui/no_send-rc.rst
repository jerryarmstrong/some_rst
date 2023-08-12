tests/ui/no_send-rc.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::rc::Rc;

fn bar<T: Send>(_: T) {}

fn main() {
    let x = Rc::new(5);
    bar(x);
    //~^ ERROR `Rc<{integer}>` cannot be sent between threads safely
}


