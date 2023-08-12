tests/ui/regions/regions-close-object-into-object-1.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]

trait A<T> { }

struct B<'a, T:'a>(&'a (A<T>+'a));

trait X { }

impl<'a, T> X for B<'a, T> {}

fn f<'a, T:'static, U>(v: Box<A<T>+'static>) -> Box<X+'static> {
    Box::new(B(&*v)) as Box<X> //~ ERROR cannot return value referencing local data `*v`
}

fn main() {}


