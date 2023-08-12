tests/ui/nll/issue-42574-diagnostic-in-nested-closure.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test illustrates a case where full NLL (enabled by the feature
// switch below) produces superior diagnostics to the NLL-migrate
// mode.

fn doit(data: &'static mut ()) {
    || doit(data);
    //~^ ERROR lifetime may not live long enough
    //~| ERROR `data` does not live long enough
}

fn main() { }


