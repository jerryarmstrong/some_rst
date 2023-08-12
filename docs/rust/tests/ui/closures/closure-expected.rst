tests/ui/closures/closure-expected.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = Some(1);
    let y = x.or_else(4);
    //~^ ERROR expected a `FnOnce<()>` closure, found `{integer}`
}


