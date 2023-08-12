tests/ui/parser/bare-struct-body.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    val: (),
}

fn foo() -> Foo { //~ ERROR struct literal body without path
    val: (),
}

fn main() {
    let x = foo();
    x.val == 42; //~ ERROR mismatched types
    let x = { //~ ERROR struct literal body without path
        val: (),
    };
}


