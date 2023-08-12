src/tools/rustfmt/tests/target/issue-3508.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<F>(foo2: F)
where
    F: Fn(
        // this comment is deleted
    ),
{
}

fn foo_block<F>(foo2: F)
where
    F: Fn(/* this comment is deleted */),
{
}

fn bar(
    bar2: impl Fn(
        // this comment is deleted
    ),
) {
}

fn bar_block(bar2: impl Fn(/* this comment is deleted */)) {}


