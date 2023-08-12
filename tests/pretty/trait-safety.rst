tests/pretty/trait-safety.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

unsafe trait UnsafeTrait {
    fn foo(&self);
}

unsafe impl UnsafeTrait for isize {
    fn foo(&self) {}
}

pub unsafe trait PubUnsafeTrait {
    fn foo(&self);
}

fn main() {}


