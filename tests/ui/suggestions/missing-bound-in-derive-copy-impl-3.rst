tests/ui/suggestions/missing-bound-in-derive-copy-impl-3.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //run-rustfix
use std::fmt::Debug;

#[derive(Debug, Copy, Clone)]
pub struct Vector2<T: Debug + Copy + Clone>{
    pub x: T,
    pub y: T
}

#[derive(Debug, Copy, Clone)] //~ ERROR the trait `Copy` may not be implemented for this type
pub struct AABB<K: Copy>{
    pub loc: Vector2<K>,
    pub size: Vector2<K>
}

fn main() {}


