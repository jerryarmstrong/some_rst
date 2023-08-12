tests/ui/traits/impl-different-num-params.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn bar(&self, x: usize) -> Self;
}
impl Foo for isize {
    fn bar(&self) -> isize {
        //~^ ERROR method `bar` has 1 parameter but the declaration in trait `Foo::bar` has 2
        *self
    }
}

fn main() {
}


