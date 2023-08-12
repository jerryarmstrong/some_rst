tests/ui/pattern/bindings-after-at/nested-binding-modes-mut.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut is_mut @ not_mut = 42;
    &mut is_mut;
    &mut not_mut;
    //~^ ERROR cannot borrow

    let not_mut @ mut is_mut = 42;
    &mut is_mut;
    &mut not_mut;
    //~^ ERROR cannot borrow
}


