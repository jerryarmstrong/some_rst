tests/ui/macros/macro-local-data-key-priv.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that the local data keys are private by default.

mod bar {
    thread_local!(static baz: f64 = 0.0);
}

fn main() {
    bar::baz.with(|_| ());
    //~^ ERROR `baz` is private
}


