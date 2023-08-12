tests/ui/feature-gates/feature-gate-inline_const_pat.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let const { () } = ();
    //~^ ERROR inline-const in pattern position is experimental [E0658]
}


