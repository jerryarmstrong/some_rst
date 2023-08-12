src/tools/rustfmt/tests/target/space-not-before-newline.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    a: (),
    // spaces ^^^ to be removed
}
enum Foo {
    Bar,
    // spaces ^^^ to be removed
}


