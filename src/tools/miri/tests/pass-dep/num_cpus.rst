src/tools/miri/tests/pass-dep/num_cpus.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-disable-isolation

fn main() {
    assert_eq!(num_cpus::get(), 1);
}


