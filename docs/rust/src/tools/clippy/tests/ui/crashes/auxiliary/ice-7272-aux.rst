src/tools/clippy/tests/ui/crashes/auxiliary/ice-7272-aux.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn warn<T>(_: T) {}

macro_rules! define_macro {
    ($d:tt $lower:ident $upper:ident) => {
        #[macro_export]
        macro_rules! $upper {
            ($arg:tt) => {
                $crate::$lower($arg)
            };
        }
    };
}

define_macro! {$ warn  WARNING}


