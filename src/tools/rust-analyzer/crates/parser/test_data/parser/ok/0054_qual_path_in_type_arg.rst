src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0054_qual_path_in_type_arg.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a() -> Foo<bar::Baz> {}

fn b(_: impl FnMut(x::Y)) {}

fn c(_: impl FnMut(&x::Y)) {}


