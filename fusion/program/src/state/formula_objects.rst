fusion/program/src/state/formula_objects.rs
===========================================

Last edited: 2022-04-29 15:13:47

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;
use crate::{Item, Ingredient};

#[account]
pub struct Formula {
    // Vector of <Ingredient> objects required to satisy the formula
    // Each <Ingredient> item is 33 bytes
    pub ingredients: Vec<Ingredient>,
    // Vector of <Item> objects to be minted on craft
    pub output_items: Vec<Item>,
}

