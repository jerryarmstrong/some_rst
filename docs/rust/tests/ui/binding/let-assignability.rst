tests/ui/binding/let-assignability.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f() {
    let a: Box<_> = Box::new(1);
    let b: &isize = &*a;
    println!("{}", b);
}

pub fn main() {
    f();
}


