tests/ui/unsized/issue-75899-but-gats.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

use std::fmt::Debug;
use std::marker::PhantomData;

trait Foo {
    type Gat<'a>: ?Sized where Self: 'a;
}

struct Bar<'a, T: Foo + 'a>(T::Gat<'a>);

struct Baz<T: ?Sized>(PhantomData<T>);

impl<T: ?Sized> Foo for Baz<T> {
    type Gat<'a> = T where Self: 'a;
}

fn main() {
    let x = Bar::<'_, Baz<()>>(());
    let y: &Bar<'_, Baz<dyn Debug>> = &x;
}


