tests/ui/impl-trait/printing-binder.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait<'a> {}
impl<T> Trait<'_> for T {}
fn whatever() -> impl for<'a> Trait<'a> + for<'b> Trait<'b> {}

fn whatever2() -> impl for<'c> Fn(&'c ()) {
    |_: &()| {}
}

fn main() {
    let x: u32 = whatever();
    //~^ ERROR mismatched types
    let x2: u32 = whatever2();
    //~^ ERROR mismatched types
}


