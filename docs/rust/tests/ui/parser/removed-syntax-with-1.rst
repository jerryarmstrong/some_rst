tests/ui/parser/removed-syntax-with-1.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    struct S {
        foo: (),
        bar: (),
    }

    let a = S { foo: (), bar: () };
    let b = S { foo: () with a, bar: () };
    //~^ ERROR expected one of `,`, `.`, `?`, `}`, or an operator, found `with`
}


