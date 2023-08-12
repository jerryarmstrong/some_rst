tests/ui/weak-new-uninhabited-issue-48493.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    enum Void {}
    let _ = std::rc::Weak::<Void>::new();
    let _ = std::sync::Weak::<Void>::new();
}


