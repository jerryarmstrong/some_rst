tests/ui/span/issue-43927-non-ADT-derive.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![derive(Debug, PartialEq, Eq)] // should be an outer attribute!
//~^ ERROR cannot determine resolution for the attribute macro `derive`
//~^^ ERROR `derive` attribute cannot be used at crate level
struct DerivedOn;

fn main() {}


