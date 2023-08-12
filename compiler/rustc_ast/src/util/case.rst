compiler/rustc_ast/src/util/case.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// Whatever to ignore case (`fn` vs `Fn` vs `FN`) or not. Used for recovering.
#[derive(Copy, Clone, Debug, Eq, PartialEq)]
pub enum Case {
    Sensitive,
    Insensitive,
}


