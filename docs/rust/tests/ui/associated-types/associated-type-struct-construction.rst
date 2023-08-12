tests/ui/associated-types/associated-type-struct-construction.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that users can construct structs through associated types
// in both expressions and patterns

#![feature(more_qualified_paths)]

// check-pass
fn main() {
    let <Foo as A>::Assoc { br } = <Foo as A>::Assoc { br: 2 };
    assert!(br == 2);
}

struct StructStruct {
    br: i8,
}

struct Foo;

trait A {
    type Assoc;
}

impl A for Foo {
    type Assoc = StructStruct;
}


