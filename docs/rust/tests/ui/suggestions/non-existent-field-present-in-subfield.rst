tests/ui/suggestions/non-existent-field-present-in-subfield.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

struct Foo {
    first: Bar,
    _second: u32,
    _third: Vec<String>,
}

struct Bar {
    bar: C,
}

struct C {
    c: D,
}

struct D {
    test: E,
}

struct E {
    _e: F,
}

struct F {
    _f: u32,
}

fn main() {
    let f = F { _f: 6 };
    let e = E { _e: f };
    let d = D { test: e };
    let c = C { c: d };
    let bar = Bar { bar: c };
    let fooer = Foo { first: bar, _second: 4, _third: Vec::new() };

    let _test = &fooer.c;
    //~^ ERROR no field

    let _test2 = fooer.test;
    //~^ ERROR no field
}


