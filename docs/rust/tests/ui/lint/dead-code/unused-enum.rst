tests/ui/lint/dead-code/unused-enum.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused)]

struct F; //~ ERROR struct `F` is never constructed
struct B; //~ ERROR struct `B` is never constructed

enum E {
    //~^ ERROR enum `E` is never used
    Foo(F),
    Bar(B),
}

fn main() {}


