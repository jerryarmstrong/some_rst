src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0012_visibility.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a() {}
pub fn b() {}
pub macro m($:ident) {}
pub(crate) fn c() {}
pub(super) fn d() {}
pub(in foo::bar::baz) fn e() {}


