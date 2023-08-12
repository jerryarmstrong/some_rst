tests/ui/associated-types/associated-types-resolve-lifetime.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

trait Get<T> {
    fn get(&self) -> T;
}

trait Trait<'a> {
    type T: 'static;
    type U: Get<&'a isize>;

    fn dummy(&'a self) { }
}

fn main() {}


