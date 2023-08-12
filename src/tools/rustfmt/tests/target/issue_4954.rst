src/tools/rustfmt/tests/target/issue_4954.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type Arg<'a>;
}

struct Bar<T>(T)
where
    for<'a> T: Foo<Arg<'a> = ()>;


