tests/ui/structs/struct-field-init-syntax.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #41834

#[derive(Default)]
struct Foo {
    one: u8,
}

fn main() {
    let foo = Foo {
        one: 111,
        ..Foo::default(),
        //~^ ERROR cannot use a comma after the base struct
    };

    let foo = Foo {
        ..Foo::default(),
        //~^ ERROR cannot use a comma after the base struct
        one: 111,
    };
}


