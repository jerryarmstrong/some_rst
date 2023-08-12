tests/ui/macros/auxiliary/two_macros-rpass.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! macro_one { ($($t:tt)*) => ($($t)*) }

#[macro_export]
macro_rules! macro_two { ($($t:tt)*) => ($($t)*) }


