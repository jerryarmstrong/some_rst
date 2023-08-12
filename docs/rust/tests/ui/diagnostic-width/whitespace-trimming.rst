tests/ui/diagnostic-width/whitespace-trimming.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-linelength

fn main() {
                                                                                                                                                                                    let _: () = 42;
//~^ ERROR mismatched types
}


