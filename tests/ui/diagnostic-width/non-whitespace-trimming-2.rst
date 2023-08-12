tests/ui/diagnostic-width/non-whitespace-trimming-2.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-linelength

fn main() {
    let _: usize = 0; let _: usize = 1; let _: usize = 2; let _: usize = 3; let _: usize = 4; let _: usize = 5; let _: usize = 6; let _: usize = 7; let _: usize = 8; let _: usize = 9; let _: usize = 10; let _: usize = 11; let _: usize = 12; let _: usize = 13; let _: usize = 14; let _: usize = 15; let _: () = 42; let _: usize = 0; let _: usize = 1; let _: usize = 2; let _: usize = 3; let _: usize = 4; let _: usize = 5; let _: usize = 6; let _: usize = 7; let _: usize = 8; let _: usize = 9; let _: usize = 10; let _: usize = 11; let _: usize = 12; let _: usize = 13; let _: usize = 14; let _: usize = 15;
//~^ ERROR mismatched types
}


