tests/ui/imports/issue-45829/rename-with-path.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::{collections::HashMap as A, sync::Arc as A};
//~^ ERROR is defined multiple times

fn main() {}


