src/tools/rust-analyzer/crates/parser/test_data/parser/err/0022_bad_exprs.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a() { [1, 2, @, struct, let] }
fn b() { foo(1, 2, @, impl, let) }
fn c() { foo.bar(1, 2, @, ], trait, let) }


