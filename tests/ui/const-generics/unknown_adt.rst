tests/ui/const-generics/unknown_adt.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _: UnknownStruct<7>;
    //~^ ERROR cannot find type `UnknownStruct`
}


