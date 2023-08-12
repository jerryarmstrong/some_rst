tests/ui/nll/user-annotations/downcast-infer.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Check that we don't try to downcast `_` when type-checking the annotation.
fn main() {
    let x = Some(Some(Some(1)));

    match x {
        Some::<Option<_>>(Some(Some(v))) => (),
        _ => (),
    }
}


