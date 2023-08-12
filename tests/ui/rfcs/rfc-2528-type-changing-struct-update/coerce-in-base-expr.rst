tests/ui/rfcs/rfc-2528-type-changing-struct-update/coerce-in-base-expr.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_changing_struct_update)]
#![allow(incomplete_features)]

use std::any::Any;

struct Foo<A, B: ?Sized, C: ?Sized> {
    a: A,
    b: Box<B>,
    c: Box<C>,
}

struct B;
struct C;

fn main() {
    let y = Foo::<usize, dyn Any, dyn Any> {
        a: 0,
        b: Box::new(B),
        ..Foo {
            a: 0,
            b: Box::new(B),
            // C needs to be told to coerce to `Box<dyn Any>`
            c: Box::new(C),
        }
    };
}


