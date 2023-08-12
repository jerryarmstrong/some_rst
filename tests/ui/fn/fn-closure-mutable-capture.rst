tests/ui/fn/fn-closure-mutable-capture.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn bar<F: Fn()>(_f: F) {} //~ NOTE change this to accept `FnMut` instead of `Fn`

pub fn foo() {
    let mut x = 0;
    bar(move || x = 1);
    //~^ ERROR cannot assign to `x`, as it is a captured variable in a `Fn` closure
    //~| NOTE cannot assign
    //~| NOTE expects `Fn` instead of `FnMut`
    //~| NOTE in this closure
}

fn main() {}


