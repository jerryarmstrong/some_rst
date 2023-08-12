tests/ui/suggestions/missing-bound-in-derive-copy-impl-2.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
use std::fmt::Debug;

#[derive(Debug, Copy, Clone)]
pub struct Vector2<T: Debug + Copy + Clone>{
    pub x: T,
    pub y: T
}

#[derive(Debug, Copy, Clone)]
pub struct AABB<K: Debug>{
    pub loc: Vector2<K>, //~ ERROR the trait bound `K: Copy` is not satisfied
    pub size: Vector2<K>
}

fn main() {}


