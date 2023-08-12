tests/ui/self/self-in-typedefs.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
#![allow(dead_code)]

use std::mem::ManuallyDrop;

enum A<'a, T: 'a>
where
    Self: Send, T: PartialEq<Self>
{
    Foo(&'a Self),
    Bar(T),
}

struct B<'a, T: 'a>
where
    Self: Send, T: PartialEq<Self>
{
    foo: &'a Self,
    bar: T,
}

union C<'a, T: 'a>
where
    Self: Send, T: PartialEq<Self>
{
    foo: &'a Self,
    bar: ManuallyDrop<T>,
}

union D<'a, T: 'a>
where
    Self: Send, T: PartialEq<Self> + Copy
{
    foo: &'a Self,
    bar: T,
}

fn main() {}


