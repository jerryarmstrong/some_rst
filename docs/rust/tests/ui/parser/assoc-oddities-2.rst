tests/ui/parser/assoc-oddities-2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z parse-only

fn main() {
    // see assoc-oddities-1 for explanation
    x..if c { a } else { b }[n]; //~ ERROR expected one of
}


