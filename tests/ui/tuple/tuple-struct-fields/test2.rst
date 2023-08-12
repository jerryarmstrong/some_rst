tests/ui/tuple/tuple-struct-fields/test2.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! define_struct {
    ($t:ty) => {
        struct S1(pub $t);
        struct S2(pub (in foo) ());
        struct S3(pub $t ());
        //~^ ERROR expected one of `)` or `,`, found `(`
    }
}

mod foo {
    define_struct! { (foo) } //~ ERROR cannot find type `foo` in this scope
                             //~| ERROR cannot find type `foo` in this scope
}

fn main() {}


