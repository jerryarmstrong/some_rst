tests/ui/lint/dead-code/unused-struct-variant.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused)]

struct F;
struct B;

enum E {
    Foo(F),
    Bar(B), //~ ERROR variant `Bar` is never constructed
}

fn main() {
    let _ = E::Foo(F);
}


