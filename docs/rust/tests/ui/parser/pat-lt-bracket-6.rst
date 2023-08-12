tests/ui/parser/pat-lt-bracket-6.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    struct Test(&'static u8, [u8; 0]);
    let x = Test(&0, []);

    let Test(&desc[..]) = x;
    //~^ ERROR: expected one of `)`, `,`, `@`, or `|`, found `[`
}

const RECOVERY_WITNESS: () = 0; //~ ERROR mismatched types


