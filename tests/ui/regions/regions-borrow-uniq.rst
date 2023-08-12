tests/ui/regions/regions-borrow-uniq.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn foo(x: &usize) -> usize {
    *x
}

pub fn main() {
    let p: Box<_> = Box::new(3);
    let r = foo(&*p);
    assert_eq!(r, 3);
}


