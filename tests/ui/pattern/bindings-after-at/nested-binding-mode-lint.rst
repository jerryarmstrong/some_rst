tests/ui/pattern/bindings-after-at/nested-binding-mode-lint.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(unused_mut)]

fn main() {
    let mut is_mut @ not_mut = 42;
    &mut is_mut;
    &not_mut;
    let not_mut @ mut is_mut = 42;
    &mut is_mut;
    &not_mut;
}


