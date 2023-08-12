tests/ui/feature-gates/feature-gate-inline_const.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = const {
        //~^ ERROR inline-const is experimental [E0658]
        true
    };
}


