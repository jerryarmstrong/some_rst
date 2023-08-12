tests/ui/macros/macro-non-lifetime.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for issue #50381: non-lifetime passed to :lifetime.

macro_rules! m { ($x:lifetime) => { } }

fn main() {
    m!(a);
    //~^ ERROR no rules expected the token `a`
}


