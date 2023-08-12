tests/ui/typeck/typeck-builtin-bound-type-parameters.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo1<T:Copy<U>, U>(x: T) {}
//~^ ERROR this trait takes 0 generic arguments but 1 generic argument was supplied

trait Trait: Copy<dyn Send> {}
//~^ ERROR this trait takes 0 generic arguments but 1 generic argument was supplied

struct MyStruct1<T: Copy<T>>;
//~^ ERROR this trait takes 0 generic arguments but 1 generic argument was supplied

struct MyStruct2<'a, T: Copy<'a>>;
//~^ ERROR this trait takes 0 lifetime arguments but 1 lifetime argument was supplied

fn foo2<'a, T:Copy<'a, U>, U>(x: T) {}
//~^ ERROR this trait takes 0 lifetime arguments but 1 lifetime argument was supplied
//~| ERROR this trait takes 0 generic arguments but 1 generic argument was supplied

fn main() { }


