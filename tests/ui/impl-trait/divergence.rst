tests/ui/impl-trait/divergence.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn foo() -> impl MyTrait {
    panic!();
    MyStruct
}

struct MyStruct;
trait MyTrait {}

impl MyTrait for MyStruct {}

fn main() {}


