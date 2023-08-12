src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0064_impl_fn_params.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl U {
    fn f1((a, b): (usize, usize)) {}
    fn f2(S { a, b }: S) {}
    fn f3(NewType(a): NewType) {}
    fn f4(&&a: &&usize) {}
}


