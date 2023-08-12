tests/ui/const-generics/array-impls/alloc-traits-impls-length-33.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub fn yes_vec_partial_eq_array<A, B>() -> impl PartialEq<[B; 33]>
where
    A: PartialEq<B>,
{
    Vec::<A>::new()
}

pub fn yes_vec_partial_eq_ref_array<'a, A, B>() -> impl PartialEq<&'a [B; 33]>
where
    A: PartialEq<B>,
{
    Vec::<A>::new()
}

use std::collections::VecDeque;

pub fn yes_vecdeque_partial_eq_array<A, B>() -> impl PartialEq<[B; 33]>
where
    A: PartialEq<B>,
{
    VecDeque::<A>::new()
}

pub fn yes_vecdeque_partial_eq_ref_array<'a, A, B>() -> impl PartialEq<&'a [B; 33]>
where
    A: PartialEq<B>,
{
    VecDeque::<A>::new()
}

pub fn yes_vecdeque_partial_eq_ref_mut_array<'a, A, B>() -> impl PartialEq<&'a mut [B; 33]>
where
    A: PartialEq<B>,
{
    VecDeque::<A>::new()
}

fn main() {}


