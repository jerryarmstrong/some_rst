tests/ui/drop-bounds/drop-bounds.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(drop_bounds)]
fn foo<T: Drop>() {} //~ ERROR
fn bar<U>()
where
    U: Drop, //~ ERROR
{
}
fn baz(_x: impl Drop) {} //~ ERROR
struct Foo<T: Drop> { //~ ERROR
  _x: T
}
struct Bar<U> where U: Drop { //~ ERROR
  _x: U
}
trait Baz: Drop { //~ ERROR
}
impl<T: Drop> Baz for T { //~ ERROR
}
fn main() {}


