tests/ui/parser/recover-tuple.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // no complaints about the tuple not matching the expected type
    let x: (usize, usize, usize) = (3, .=.);
    //~^ ERROR expected expression, found `.`
    // verify that the parser recovers:
    let y: usize = ""; //~ ERROR mismatched types
    // no complaints about the type
    foo(x);
}

fn foo(_: (usize, usize, usize)) {}


