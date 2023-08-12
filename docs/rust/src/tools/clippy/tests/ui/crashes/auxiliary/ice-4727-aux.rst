src/tools/clippy/tests/ui/crashes/auxiliary/ice-4727-aux.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Trait {
    fn fun(par: &str) -> &str;
}

impl Trait for str {
    fn fun(par: &str) -> &str {
        &par[0..1]
    }
}


