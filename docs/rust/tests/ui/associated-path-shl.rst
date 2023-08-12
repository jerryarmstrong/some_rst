tests/ui/associated-path-shl.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that associated paths starting with `<<` are successfully parsed.

fn main() {
    let _: <<A>::B>::C; //~ ERROR cannot find type `A` in this scope
    let _ = <<A>::B>::C; //~ ERROR cannot find type `A` in this scope
    let <<A>::B>::C; //~ ERROR cannot find type `A` in this scope
    let 0 ..= <<A>::B>::C; //~ ERROR cannot find type `A` in this scope
    <<A>::B>::C; //~ ERROR cannot find type `A` in this scope
}


