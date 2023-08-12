tests/ui/consts/const-nullary-univariant-enum.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(Copy, Clone)]
enum Foo {
    Bar = 0xDEADBEE
}

static X: Foo = Foo::Bar;

pub fn main() {
    assert_eq!((X as usize), 0xDEADBEE);
    assert_eq!((Y as usize), 0xDEADBEE);
}

static Y: Foo = Foo::Bar;


