tests/ui/unique/unique-fn-ret.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f() -> Box<isize> {
    Box::new(100)
}

pub fn main() {
    assert_eq!(f(), Box::new(100));
}


