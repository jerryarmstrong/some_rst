tests/ui/issues/issue-7061.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct BarStruct;

impl<'a> BarStruct {
    fn foo(&'a mut self) -> Box<BarStruct> { self }
    //~^ ERROR mismatched types
    //~| expected struct `Box<BarStruct>`
    //~| found mutable reference `&'a mut BarStruct`
}

fn main() {}


