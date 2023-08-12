tests/ui/lint/known-tool-in-submodule/root.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(register_tool)]
#![register_tool(tool)]

mod submodule;

fn main() {
    submodule::foo();
}


