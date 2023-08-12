tests/ui/diagnostic-width/whitespace-trimming-2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-linelength

fn foo() -> usize {
                                                                                                                                                                                          ()
//~^ ERROR mismatched types
}

fn main() {}


