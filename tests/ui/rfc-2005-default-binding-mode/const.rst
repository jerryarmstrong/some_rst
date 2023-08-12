tests/ui/rfc-2005-default-binding-mode/const.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // FIXME(tschottdorf): this test should pass.

#[derive(PartialEq, Eq)]
struct Foo {
    bar: i32,
}

const FOO: Foo = Foo{bar: 5};

fn main() {
    let f = Foo{bar:6};

    match &f {
        FOO => {}, //~ ERROR mismatched types
        _ => panic!(),
    }
}


