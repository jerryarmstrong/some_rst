tests/ui/regions/owned-implies-static.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn f<T: 'static>(_x: T) {}

pub fn main() {
    f(Box::new(5));
}


