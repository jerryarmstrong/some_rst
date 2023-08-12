tests/ui/regions/regions-borrow-at.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn foo(x: &usize) -> usize {
    *x
}

pub fn main() {
    let p: Box<_> = Box::new(22);
    let r = foo(&*p);
    println!("r={}", r);
    assert_eq!(r, 22);
}


