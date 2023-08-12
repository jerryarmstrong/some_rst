tests/ui/kindck/kindck-nonsendable-1.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::rc::Rc;

fn foo(_x: Rc<usize>) {}

fn bar<F:FnOnce() + Send>(_: F) { }

fn main() {
    let x = Rc::new(3);
    bar(move|| foo(x));
    //~^ ERROR `Rc<usize>` cannot be sent between threads safely
}


