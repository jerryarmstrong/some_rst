tests/ui/parser/type-parameters-in-field-exprs.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    x: isize,
    y: isize,
}

fn main() {
    let f = Foo {
        x: 1,
        y: 2,
    };
    f.x::<isize>;
    //~^ ERROR field expressions cannot have generic arguments
    f.x::<>;
    //~^ ERROR field expressions cannot have generic arguments
    f.x::();
    //~^ ERROR field expressions cannot have generic arguments
}


