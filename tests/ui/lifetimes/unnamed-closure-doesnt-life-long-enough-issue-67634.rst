tests/ui/lifetimes/unnamed-closure-doesnt-life-long-enough-issue-67634.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    [0].iter().flat_map(|a| [0].iter().map(|_| &a)); //~ ERROR closure may outlive
}


