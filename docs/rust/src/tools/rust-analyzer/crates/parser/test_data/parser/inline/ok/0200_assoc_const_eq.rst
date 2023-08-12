src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0200_assoc_const_eq.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<F: Foo<N=3>>() {}
const TEST: usize = 3;
fn bar<F: Foo<N={TEST}>>() {}


