tests/ui/issues/auxiliary/issue-4545.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct S<T>(Option<T>);
pub fn mk<T>() -> S<T> { S(None) }


