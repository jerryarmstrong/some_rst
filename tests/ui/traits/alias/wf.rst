tests/ui/traits/alias/wf.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_alias)]

trait Foo {}
trait A<T: Foo> {}
trait B<T> = A<T>; //~ ERROR `T: Foo` is not satisfied

fn main() {}


