tests/ui/resolve/point-at-type-parameter-shadowing-another-type.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo<T> {
    fn foo(&self, name: T) -> usize;
}

struct Bar {
    baz: Baz,
}

struct Baz {
    num: usize,
}

impl<Baz> Foo<Baz> for Bar {
    fn foo(&self, _name: Baz) -> usize {
        match self.baz {
            Baz { num } => num, //~ ERROR expected struct, variant or union type, found type parameter `Baz`
        }
    }
}

fn main() {}


