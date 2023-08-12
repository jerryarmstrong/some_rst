tests/ui/chalkify/super_trait.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Z trait-solver=chalk

trait Foo { }
trait Bar: Foo { }

impl Foo for i32 { }
impl Bar for i32 { }

fn only_foo<T: Foo>() { }

fn only_bar<T: Bar>() {
    // `T` implements `Bar` hence `T` must also implement `Foo`
    only_foo::<T>()
}

fn main() {
    only_bar::<i32>()
}


