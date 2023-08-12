tests/ui/generic-associated-types/generic-associated-types-where.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checking the interaction with this other feature
#![feature(associated_type_defaults)]

use std::fmt::{Display, Debug};

trait Foo {
    type Assoc where Self: Sized;
    type Assoc2<T> where T: Display;
    type Assoc3<T>;
    type WithDefault<'a, T: Debug + 'a>: ?Sized = dyn Iterator<Item=T>;
    type NoGenerics;
}

struct Bar;

impl Foo for Bar {
    type Assoc = usize;
    type Assoc2<T> = Vec<T>;
    //~^ ERROR `T` doesn't implement `std::fmt::Display`
    type Assoc3<T> = Vec<T> where T: Iterator;
    //~^ ERROR impl has stricter requirements than trait
    type WithDefault<'a, T: Debug + 'a> = &'a dyn Iterator<Item=T>;
    type NoGenerics = ::std::cell::Cell<i32>;
}

fn main() {}


