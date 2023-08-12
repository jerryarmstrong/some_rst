tests/ui/shadowed/shadowing-in-the-same-pattern.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for issue #14581.

fn f((a, a): (isize, isize)) {} //~ ERROR identifier `a` is bound more than once

fn main() {
    let (a, a) = (1, 1);    //~ ERROR identifier `a` is bound more than once
}


