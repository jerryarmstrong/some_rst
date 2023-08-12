tests/ui/resolve/block-with-trait-parent.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Trait {
    fn method(&self) {
        // Items inside a block turn it into a module internally.
        struct S;
        impl Trait for S {}

        // OK, `Trait` is in scope here from method resolution point of view.
        S.method();
    }
}

fn main() {}


