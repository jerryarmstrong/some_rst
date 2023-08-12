tests/ui/static/static-region-bound.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn id<T>(x: T) -> T { x }

fn f<T:'static>(_: T) {}

fn main() {

    let x: Box<_> = Box::new(3);
    f(x);

    let x = &id(3); //~ ERROR temporary value dropped while borrowed
    f(x);
}


