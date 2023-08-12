tests/ui/lint/must_not_suspend/tuple-mismatch.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

fn main() {
    let _generator = || {
        yield ((), ((), ()));
        yield ((), ());
        //~^ ERROR mismatched types
    };
}


