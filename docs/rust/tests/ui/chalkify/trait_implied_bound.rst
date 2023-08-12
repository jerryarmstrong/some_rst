tests/ui/chalkify/trait_implied_bound.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Z trait-solver=chalk

trait Foo { }
trait Bar<U> where U: Foo { }

impl Foo for i32 { }
impl Bar<i32> for i32 { }

fn only_foo<T: Foo>() { }

fn only_bar<U, T: Bar<U>>() {
    only_foo::<U>()
}

fn main() {
    only_bar::<i32, i32>()
}


