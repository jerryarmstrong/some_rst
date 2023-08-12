tests/ui/module-macro_use-arguments.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use(foo, bar)] //~ ERROR arguments to `macro_use` are not allowed here
mod foo {
}

fn main() {
}


