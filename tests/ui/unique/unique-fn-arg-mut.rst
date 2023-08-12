tests/ui/unique/unique-fn-arg-mut.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f(i: &mut Box<isize>) {
    *i = Box::new(200);
}

pub fn main() {
    let mut i = Box::new(100);
    f(&mut i);
    assert_eq!(*i, 200);
}


