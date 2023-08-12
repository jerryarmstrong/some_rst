src/tools/rustfmt/tests/source/issue-4984/multiple_comments_within.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(
/* ---------- Some really important comment that just had to go inside the derive --------- */
Debug, Clone,/* Another comment */Eq, PartialEq,
)]
struct Foo {
    a: i32,
    b: T,
}


