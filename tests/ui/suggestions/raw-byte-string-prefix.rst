tests/ui/suggestions/raw-byte-string-prefix.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // `br` and `rb` are easy to confuse; check that we issue a suggestion to help.

// edition:2021

fn main() {
    rb"abc";
    //~^ ERROR: prefix `rb` is unknown
    //~| HELP: use `br` for a raw byte string
    //~| ERROR: expected one of
}


