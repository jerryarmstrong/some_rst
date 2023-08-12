tests/ui/let-else/let-else-source-expr-nomove-pass.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// issue #89688



fn example_let_else(value: Option<String>) {
    let Some(inner) = value else {
        println!("other: {:?}", value); // OK
        return;
    };
    println!("inner: {}", inner);
}

fn main() {
    example_let_else(Some("foo".into()));
    example_let_else(None);
}


