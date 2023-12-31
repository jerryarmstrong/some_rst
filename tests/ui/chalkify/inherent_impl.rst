tests/ui/chalkify/inherent_impl.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Z trait-solver=chalk

trait Foo { }

impl Foo for i32 { }

struct S<T: Foo> {
    x: T,
}

fn only_foo<T: Foo>(_x: &T) { }

impl<T> S<T> {
    // Test that we have the correct environment inside an inherent method.
    fn dummy_foo(&self) {
        only_foo(&self.x)
    }
}

trait Bar { }
impl Bar for u32 { }

fn only_bar<T: Bar>() { }

impl<T> S<T> {
    // Test that the environment of `dummy_bar` adds up with the environment
    // of the inherent impl.
    fn dummy_bar<U: Bar>(&self) {
        only_foo(&self.x);
        only_bar::<U>();
    }
}

fn main() {
    let s = S {
        x: 5,
    };

    s.dummy_bar::<u32>();
    s.dummy_foo();
}


