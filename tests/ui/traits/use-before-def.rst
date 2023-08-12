tests/ui/traits/use-before-def.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

// Issue #1761

// pretty-expanded FIXME #23616

impl foo for isize { fn foo(&self) -> isize { 10 } }
trait foo { fn foo(&self) -> isize; }
pub fn main() {}


