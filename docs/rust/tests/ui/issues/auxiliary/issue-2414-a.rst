tests/ui/issues/auxiliary/issue-2414-a.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="a"]
#![crate_type = "lib"]

type t1 = usize;

trait foo {
    fn foo(&self);
}

impl foo for String {
    fn foo(&self) {}
}


