tests/ui/dst/dst-sized-trait-param.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that when you implement a trait that has a sized type
// parameter, the corresponding value must be sized. Also that the
// self type must be sized if appropriate.

trait Foo<T> : Sized { fn take(self, x: &T) { } } // Note: T is sized

impl Foo<[isize]> for usize { }
//~^ ERROR the size for values of type

impl Foo<isize> for [usize] { }
//~^ ERROR the size for values of type

pub fn main() { }


