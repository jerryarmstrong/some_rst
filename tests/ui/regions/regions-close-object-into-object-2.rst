tests/ui/regions/regions-close-object-into-object-2.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A<T> { }

struct B<'a, T:'a>(&'a (dyn A<T> + 'a));

trait X { }
impl<'a, T> X for B<'a, T> {}

fn g<'a, T: 'static>(v: Box<dyn A<T> + 'a>) -> Box<dyn X + 'static> {
    Box::new(B(&*v)) as Box<dyn X>
    //~^ ERROR lifetime may not live long enough
    //~| ERROR cannot return value referencing local data `*v` [E0515]
}

fn main() { }


