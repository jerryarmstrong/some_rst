tests/ui/associated-types/point-at-type-on-obligation-failure-2.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Bar {}

trait Foo {
    type Assoc: Bar;
}

impl Foo for () {
    type Assoc = bool; //~ ERROR the trait bound `bool: Bar` is not satisfied
}

trait Baz
where
    Self::Assoc: Bar,
{
    type Assoc;
}

impl Baz for () {
    type Assoc = bool; //~ ERROR the trait bound `bool: Bar` is not satisfied
}

trait Bat
where
    <Self as Bat>::Assoc: Bar,
{
    type Assoc;
}

impl Bat for () {
    type Assoc = bool; //~ ERROR the trait bound `bool: Bar` is not satisfied
}

fn main() {}


