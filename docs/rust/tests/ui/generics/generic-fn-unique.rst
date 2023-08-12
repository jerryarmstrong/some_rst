tests/ui/generics/generic-fn-unique.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f<T>(x: Box<T>) -> Box<T> { return x; }

pub fn main() {
    let x = f(Box::new(3));
    println!("{}", *x);
}


