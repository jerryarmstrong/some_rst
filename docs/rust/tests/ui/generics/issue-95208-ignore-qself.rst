tests/ui/generics/issue-95208-ignore-qself.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[allow(unused)]
struct Struct<T>(T);

impl<T: Iterator> Struct<T> where <T as std:: iter::Iterator>::Item:: std::fmt::Display {
//~^ ERROR expected `:` followed by trait or lifetime
//~| HELP use single colon
}

fn main() {}


