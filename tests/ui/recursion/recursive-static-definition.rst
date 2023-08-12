tests/ui/recursion/recursive-static-definition.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub static FOO: u32 = FOO;
//~^ ERROR cycle detected when const-evaluating + checking `FOO`

fn main() {}


