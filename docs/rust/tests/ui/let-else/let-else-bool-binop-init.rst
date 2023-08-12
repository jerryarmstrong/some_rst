tests/ui/let-else/let-else-bool-binop-init.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix



fn main() {
    let true = true && false else { return }; //~ ERROR a `&&` expression cannot be directly assigned in `let...else`
    let true = true || false else { return }; //~ ERROR a `||` expression cannot be directly assigned in `let...else`
}


