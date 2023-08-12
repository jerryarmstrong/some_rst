tests/ui/builtin-superkinds/builtin-superkinds-simple2.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Simple test case of implementing a trait with super-builtin-kinds.

// pretty-expanded FIXME #23616

trait Foo : Send { }

impl Foo for isize { }

pub fn main() { }


