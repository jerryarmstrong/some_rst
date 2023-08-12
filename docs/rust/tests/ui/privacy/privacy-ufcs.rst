tests/ui/privacy/privacy-ufcs.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test to ensure private traits are inaccessible with UFCS angle-bracket syntax.

mod foo {
    trait Bar {
        fn baz() {}
    }

    impl Bar for i32 {}
}

fn main() {
    <i32 as ::foo::Bar>::baz(); //~ERROR trait `Bar` is private
}


