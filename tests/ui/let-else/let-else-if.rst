tests/ui/let-else/let-else-if.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let Some(_) = Some(()) else if true {
        //~^ ERROR conditional `else if` is not supported for `let...else`
        return;
    } else {
        return;
    };
}


