tests/ui/parser/issues/issue-8537.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub extern
  "invalid-ab_isize" //~ ERROR invalid ABI
fn foo() {}

fn main() {}


