tests/ui/issues/issue-6738.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<T> {
    x: T,
}
impl<T> Foo<T> {
    fn add(&mut self, v: Foo<T>){
        self.x += v.x;
        //~^ ERROR: binary assignment operation `+=` cannot be applied
    }
}
fn main() {}


