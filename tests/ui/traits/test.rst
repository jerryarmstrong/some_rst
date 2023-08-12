tests/ui/traits/test.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(non_camel_case_types)]
trait foo { fn foo(&self); }

impl isize for usize { fn foo(&self) {} } //~ ERROR trait

fn main() {}


