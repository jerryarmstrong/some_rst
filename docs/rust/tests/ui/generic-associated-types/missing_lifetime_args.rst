tests/ui/generic-associated-types/missing_lifetime_args.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X {
    type Y<'a, 'b>;
}

struct Foo<'a, 'b, 'c> {
    a: &'a u32,
    b: &'b str,
    c: &'c str,
}

fn foo<'c, 'd>(_arg: Box<dyn X<Y = (&'c u32, &'d u32)>>) {}
//~^ ERROR missing generics for associated type

fn bar<'a, 'b, 'c>(_arg: Foo<'a, 'b>) {}
//~^ ERROR this struct takes 3 lifetime arguments but 2 lifetime

fn f<'a>(_arg: Foo<'a>) {}
//~^ ERROR this struct takes 3 lifetime arguments but 1 lifetime

fn main() {}


