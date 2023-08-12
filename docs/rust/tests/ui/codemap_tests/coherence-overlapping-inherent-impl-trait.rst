tests/ui/codemap_tests/coherence-overlapping-inherent-impl-trait.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

trait C {}
impl dyn C { fn f() {} } //~ ERROR duplicate
impl dyn C { fn f() {} }
fn main() { }


