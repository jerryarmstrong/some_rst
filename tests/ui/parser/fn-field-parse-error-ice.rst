tests/ui/parser/fn-field-parse-error-ice.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #85794

struct Baz {
    inner : dyn fn ()
    //~^ ERROR expected `,`, or `}`, found keyword `fn`
    //~| ERROR expected identifier, found keyword `fn`
    //~| ERROR cannot find type `dyn` in this scope
}

fn main() {}


