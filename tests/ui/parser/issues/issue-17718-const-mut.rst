tests/ui/parser/issues/issue-17718-const-mut.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const
mut //~ ERROR: const globals cannot be mutable
//~^^ HELP you might want to declare a static instead
FOO: usize = 3;

fn main() {
}


