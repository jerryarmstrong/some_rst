tests/ui/parser/trailing-carriage-return-in-string.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #11669

// ignore-tidy-cr

fn main() {
    // \r\n
    let ok = "This is \
 a test";
    // \r only
    let bad = "This is \ a test";
    //~^ ERROR unknown character escape: `\r`
    //~| HELP this is an isolated carriage return

}


