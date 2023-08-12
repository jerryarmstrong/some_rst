tests/ui/nll/self-assign-ref-mut.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that `*y` isn't borrowed after `y = y`.

// check-pass

fn main() {
    let mut x = 1;
    {
        let mut y = &mut x;
        y = y;
        y;
    }
    x;
    {
        let mut y = &mut x;
        y = y;
        y = y;
        y;
    }
    x;
}


