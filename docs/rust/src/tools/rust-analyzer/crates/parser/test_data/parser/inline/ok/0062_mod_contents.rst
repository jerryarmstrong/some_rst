src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0062_mod_contents.rs
=====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {}
macro_rules! foo {}
foo::bar!();
super::baz! {}
struct S;


