tests/ui/let-else/let-else-missing-semicolon.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let Some(x) = Some(1) else {
        return;
    } //~ ERROR expected `;`, found keyword `let`
    let _ = "";
    let Some(x) = Some(1) else {
        panic!();
    } //~ ERROR expected `;`, found `}`
}


