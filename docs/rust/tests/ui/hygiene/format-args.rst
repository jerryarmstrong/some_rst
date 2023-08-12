tests/ui/hygiene/format-args.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(non_upper_case_globals)]
#![feature(format_args_nl)]

static arg0: () = ();

fn main() {
    static arg1: () = ();
    format_args!("{} {:?}", 0, 1);
    format_args_nl!("{} {:?}", 0, 1);
}


