tests/ui/parser/pat-lt-bracket-7.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    struct Thing(u8, [u8; 0]);
    let foo = core::iter::empty();

    for Thing(x[]) in foo {}
    //~^ ERROR: expected one of `)`, `,`, `@`, or `|`, found `[`
}

const RECOVERY_WITNESS: () = 0; //~ ERROR mismatched types


