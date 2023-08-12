tests/ui/or-patterns/basic-switch.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test basic or-patterns when the target pattern type will be lowered to a
// `Switch` (an `enum`).

// run-pass

#[derive(Debug)]
enum Test {
    Foo,
    Bar,
    Baz,
    Qux,
}

fn test(x: Option<Test>) -> bool {
    match x {
        // most simple case
        Some(Test::Bar | Test::Qux) => true,
        // wild case
        Some(_) => false,
        // empty case
        None => false,
    }
}

fn main() {
    assert!(!test(Some(Test::Foo)));
    assert!(test(Some(Test::Bar)));
    assert!(!test(Some(Test::Baz)));
    assert!(test(Some(Test::Qux)));
    assert!(!test(None))
}


