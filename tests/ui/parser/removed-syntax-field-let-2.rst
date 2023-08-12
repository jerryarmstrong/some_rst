tests/ui/parser/removed-syntax-field-let-2.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    let x: i32,
    //~^ ERROR expected identifier, found keyword
    let y: i32,
    //~^ ERROR expected identifier, found keyword
}

fn main() {
    let _ = Foo {
        //~^ ERROR missing fields `x` and `y` in initializer of `Foo`
    };
}


