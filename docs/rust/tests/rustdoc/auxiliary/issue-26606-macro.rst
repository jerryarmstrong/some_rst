tests/rustdoc/auxiliary/issue-26606-macro.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! make_item (
    ($name: ident) => (pub const $name: usize = 42;)
);


