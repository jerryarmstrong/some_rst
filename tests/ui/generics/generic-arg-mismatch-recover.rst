tests/ui/generics/generic-arg-mismatch-recover.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<'a, T: 'a>(&'a T);

struct Bar<'a>(&'a ());

fn main() {
    Foo::<'static, 'static, ()>(&0);
    //~^ ERROR this struct takes 1 lifetime argument but 2 lifetime arguments were supplied

    Bar::<'static, 'static, ()>(&());
    //~^ ERROR this struct takes 1 lifetime argument but 2 lifetime arguments were supplied
    //~| ERROR this struct takes 0
}


