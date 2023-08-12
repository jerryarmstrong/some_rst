src/tools/rustfmt/tests/target/issue-5011.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub(crate) struct ASlash(
    // hello
    i32,
);

pub(crate) struct AStar(/* hello */ i32);

pub(crate) struct BStar(/* hello */ i32);


