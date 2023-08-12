tests/ui/structs-enums/struct-lit-functional-no-fields.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[derive(Debug,PartialEq,Clone)]
struct Foo<T> {
    bar: T,
    baz: T
}

pub fn main() {
    let foo = Foo {
        bar: 0,
        baz: 1
    };

    let foo_ = foo.clone();
    let foo = Foo { ..foo };
    assert_eq!(foo, foo_);

    let foo = Foo {
        bar: "one".to_string(),
        baz: "two".to_string()
    };

    let foo_ = foo.clone();
    let foo = Foo { ..foo };
    assert_eq!(foo, foo_);
}


