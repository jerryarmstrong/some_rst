tests/ui/generator/unresolved-ct-var-drop-tracking.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // incremental
// edition:2021
// compile-flags: -Zdrop-tracking

fn main() {
    let _ = async {
        let s = std::array::from_fn(|_| ()).await;
        //~^ ERROR `[(); _]` is not a future
        //~| ERROR type inside `async` block must be known in this context
        //~| ERROR type inside `async` block must be known in this context
        //~| ERROR type inside `async` block must be known in this context
        //~| ERROR type inside `async` block must be known in this context
        //~| ERROR type inside `async` block must be known in this context
    };
}


