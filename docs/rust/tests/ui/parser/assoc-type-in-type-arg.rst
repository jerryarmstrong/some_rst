tests/ui/parser/assoc-type-in-type-arg.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Tr {
    type TrSubtype;
}

struct Bar<'a, Item: Tr, <Item as Tr>::TrSubtype: 'a> {
    //~^ ERROR bounds on associated types do not belong here
    item: Item,
    item_sub: &'a <Item as Tr>::TrSubtype,
}

fn main() {}


