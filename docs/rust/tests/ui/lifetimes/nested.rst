tests/ui/lifetimes/nested.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn method<'a>(_i: &'a i32) {
    fn inner<'a>(_j: &'a f32) {}
}

fn main() {}


