src/tools/miri/tests/pass/shims/env/var-without-isolation.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-disable-isolation

fn main() {
    assert_eq!(std::env::var("MIRI_ENV_VAR_TEST"), Ok("0".to_owned()));
}


