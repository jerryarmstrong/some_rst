src/tools/rustfmt/tests/target/issue-2103.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X
where
    i32: Sized,
{
    x: i32,
}

struct X
// with comment
where
    i32: Sized,
{
    x: i32,
}


