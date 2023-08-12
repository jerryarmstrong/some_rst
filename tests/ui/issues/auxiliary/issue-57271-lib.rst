tests/ui/issues/auxiliary/issue-57271-lib.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Copy, Clone, Debug, Eq, PartialEq, Hash)]
pub enum BaseType {
    Byte,
    Char,
    Double,
    Float,
    Int,
    Long,
    Short,
    Boolean,
}


