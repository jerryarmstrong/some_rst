tests/ui/rfc-2632-const-trait-impl/const-drop-bound.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(const_trait_impl)]
#![feature(const_precise_live_drops)]

use std::marker::Destruct;

const fn foo<T, E>(res: Result<T, E>) -> Option<T> where E: ~const Destruct {
    match res {
        Ok(t) => Some(t),
        Err(_e) => None,
    }
}

pub struct Foo<T>(T);

const fn baz<T, E>(res: Result<Foo<T>, Foo<E>>) -> Option<Foo<T>>
where
    T: ~const Destruct,
    E: ~const Destruct,
{
    foo(res)
}

fn main() {}


