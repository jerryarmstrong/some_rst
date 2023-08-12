language/move-borrow-graph/src/paths.rs
=======================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

pub type PathSlice<Lbl> = [Lbl];
pub type Path<Lbl> = Vec<Lbl>;

pub fn leq<Lbl: Eq>(lhs: &PathSlice<Lbl>, rhs: &PathSlice<Lbl>) -> bool {
    lhs.len() <= rhs.len() && lhs.iter().zip(rhs).all(|(l, r)| l == r)
}

pub fn factor<Lbl: Eq>(lhs: &PathSlice<Lbl>, mut rhs: Path<Lbl>) -> (Path<Lbl>, Path<Lbl>) {
    assert!(leq(lhs, &rhs));
    let suffix = rhs.split_off(lhs.len());
    (rhs, suffix)
}

pub fn append<Lbl: Clone>(lhs: &PathSlice<Lbl>, rhs: &PathSlice<Lbl>) -> Path<Lbl> {
    let mut path: Path<Lbl> = lhs.into();
    path.append(&mut rhs.to_owned());
    path
}


