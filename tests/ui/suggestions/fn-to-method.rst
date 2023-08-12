tests/ui/suggestions/fn-to-method.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

impl Foo {
    fn bar(self) {}
}

fn main() {
    let x = cmp(&1, &2);
    //~^ ERROR cannot find function `cmp` in this scope
    //~| HELP use the `.` operator to call the method `Ord::cmp` on `&{integer}`

    let y = len([1, 2, 3]);
    //~^ ERROR cannot find function `len` in this scope
    //~| HELP use the `.` operator to call the method `len` on `&[{integer}]`

    let z = bar(Foo);
    //~^ ERROR cannot find function `bar` in this scope
    //~| HELP use the `.` operator to call the method `bar` on `Foo`
}


