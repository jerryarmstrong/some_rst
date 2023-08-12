tests/ui/associated-consts/associated-const-in-global-const.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Foo;

impl Foo {
    const BAR: f32 = 1.5;
}

const FOOBAR: f32 = <Foo>::BAR;

fn main() {
    assert_eq!(1.5f32, FOOBAR);
}


