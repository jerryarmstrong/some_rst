tests/ui/derives/deriving-bounds.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Send)]
//~^ ERROR cannot find derive macro `Send` in this scope
//~| ERROR cannot find derive macro `Send` in this scope
struct Test;

#[derive(Sync)]
//~^ ERROR cannot find derive macro `Sync` in this scope
//~| ERROR cannot find derive macro `Sync` in this scope
struct Test1;

pub fn main() {}


