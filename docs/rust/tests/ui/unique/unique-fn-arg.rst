tests/ui/unique/unique-fn-arg.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f(i: Box<isize>) {
    assert_eq!(*i, 100);
}

pub fn main() {
    f(Box::new(100));
    let i = Box::new(100);
    f(i);
}


