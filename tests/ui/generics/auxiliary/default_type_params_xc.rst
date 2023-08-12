tests/ui/generics/auxiliary/default_type_params_xc.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Heap;

pub struct FakeHeap;

pub struct FakeVec<T, A = FakeHeap> { pub f: Option<(T,A)> }


