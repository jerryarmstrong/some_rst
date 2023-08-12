tests/ui/macros/macro-missing-fragment-deduplication.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zdeduplicate-diagnostics=yes

macro_rules! m {
    ($name) => {}
    //~^ ERROR missing fragment
    //~| ERROR missing fragment
    //~| WARN this was previously accepted
}

fn main() {
    m!();
    m!();
    m!();
    m!();
}


