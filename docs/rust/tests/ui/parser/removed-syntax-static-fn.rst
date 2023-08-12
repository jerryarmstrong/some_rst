tests/ui/parser/removed-syntax-static-fn.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;

impl S {
    static fn f() {}
    //~^ ERROR expected identifier, found keyword `fn`
    //~| ERROR expected one of `:`, `;`, or `=`
    //~| ERROR missing type for `static` item
}

fn main() {}


