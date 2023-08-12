tests/ui/parser/recovered-struct-variant.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo {
    A { a, b: usize }
    //~^ ERROR expected `:`, found `,`
}

fn main() {
    // no complaints about non-existing fields
    let f = Foo::A { a:3, b: 4};
    match f {
        // no complaints about non-existing fields
        Foo::A {a, b} => {}
    }
}


