tests/ui/unique/unique-assign-generic.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f<T>(t: T) -> T {
    let t1 = t;
    t1
}

pub fn main() {
    let t = f::<Box<_>>(Box::new(100));
    assert_eq!(t, Box::new(100));
}


