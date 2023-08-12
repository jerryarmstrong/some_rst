tests/ui/borrowck/issue-53432-nested-closure-outlives-borrowed-value.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let f = move || {};
    let _action = move || {
        || f() // The `nested` closure
        //~^ ERROR lifetime may not live long enough
    };
}


