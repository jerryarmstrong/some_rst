src/tools/rustfmt/tests/target/issue_4545.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Debug, Foo<T>)]
enum Bar {}

#[derive(Debug, , Default)]
struct Struct(i32);


