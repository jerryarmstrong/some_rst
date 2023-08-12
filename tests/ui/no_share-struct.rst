tests/ui/no_share-struct.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

use std::marker::Sync;

struct Foo { a: isize }
impl !Sync for Foo {}

fn bar<T: Sync>(_: T) {}

fn main() {
    let x = Foo { a: 5 };
    bar(x);
    //~^ ERROR `Foo` cannot be shared between threads safely [E0277]
}


