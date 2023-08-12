src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0063_trait_fn_patterns.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
    fn f1((a, b): (usize, usize)) {}
    fn f2(S { a, b }: S) {}
    fn f3(NewType(a): NewType) {}
    fn f4(&&a: &&usize) {}
    fn bar(_: u64, mut x: i32);
}


