tests/ui/diagnostic-width/non-whitespace-trimming.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-linelength

fn main() {
    let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = 42; let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = (); let _: () = ();
//~^ ERROR mismatched types
}


