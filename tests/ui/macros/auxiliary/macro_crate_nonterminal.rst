tests/ui/macros/auxiliary/macro_crate_nonterminal.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn increment(x: usize) -> usize {
    x + 1
}

#[macro_export]
macro_rules! increment {
    ($x:expr) => ($crate::increment($x))
}

pub fn check_local() {
    assert_eq!(increment!(3), 4);
}


