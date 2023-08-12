tests/ui/generics/generic-type-synonym.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]


// pretty-expanded FIXME #23616

struct Foo<T> {
    a: T
}

type Bar<T> = Foo<T>;

fn takebar<T>(_b: Bar<T>) { }

pub fn main() { }


