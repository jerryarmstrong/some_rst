tests/ui/tuple/tuple-struct-fields/test.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    type T = ();
    struct S1(pub(in foo) (), pub(T), pub(crate) (), pub(((), T)));
    struct S2(pub((foo)) ());
    //~^ ERROR expected one of `)` or `,`, found `(`
    //~| ERROR cannot find type `foo` in this scope
}

fn main() {}


