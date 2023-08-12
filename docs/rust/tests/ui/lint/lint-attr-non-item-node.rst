tests/ui/lint/lint-attr-non-item-node.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that lint attributes work on non-item AST nodes

fn main() {
    #[deny(unreachable_code)]
    loop {
        break;
        "unreachable"; //~ ERROR unreachable statement
    }
}


