tests/ui/nll/issue-69114-static-ty.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that borrowck ensures that `static` items have the expected type.

static FOO: &'static (dyn Fn(&'static u8) + Send + Sync) = &drop;

fn main() {
    let n = 42;
    FOO(&n);
    //~^ ERROR does not live long enough
}


