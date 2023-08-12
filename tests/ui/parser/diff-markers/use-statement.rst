tests/ui/parser/diff-markers/use-statement.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use foo::{
<<<<<<< HEAD //~ ERROR encountered diff marker
    bar,
=======
    baz,
>>>>>>> branch
};

fn main() {}


