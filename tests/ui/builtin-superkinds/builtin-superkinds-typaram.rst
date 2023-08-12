tests/ui/builtin-superkinds/builtin-superkinds-typaram.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests correct implementation of traits with super-builtin-kinds
// using a bounded type parameter.

// pretty-expanded FIXME #23616

trait Foo : Send { }

impl <T: Send> Foo for T { }

pub fn main() { }


