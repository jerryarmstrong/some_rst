tests/ui/consts/const-try-feature-gate.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-const_try

const fn t() -> Option<()> {
    Some(())?;
    //~^ error: `?` is not allowed in a `const fn`
    None
}

fn main() {}


