src/tools/rustfmt/tests/target/issue-5151/minimum_example.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(more_qualified_paths)]

struct Struct {}

trait Trait {
    type Type;
}

impl Trait for Struct {
    type Type = Self;
}

fn main() {
    // keep the qualified path details
    let _ = <Struct as Trait>::Type {};
}


