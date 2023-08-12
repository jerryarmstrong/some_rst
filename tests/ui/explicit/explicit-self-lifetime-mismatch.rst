tests/ui/explicit/explicit-self-lifetime-mismatch.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<'a,'b> {
    x: &'a isize,
    y: &'b isize,
}

impl<'a,'b> Foo<'a,'b> {
    fn bar(self:
           Foo<'b,'a>
    //~^ ERROR mismatched `self` parameter type
    //~| expected struct `Foo<'a, 'b>`
    //~| found struct `Foo<'b, 'a>`
    //~| lifetime mismatch
    //~| ERROR mismatched `self` parameter type
    //~| expected struct `Foo<'a, 'b>`
    //~| found struct `Foo<'b, 'a>`
    //~| lifetime mismatch
           ) {}
}

fn main() {}


