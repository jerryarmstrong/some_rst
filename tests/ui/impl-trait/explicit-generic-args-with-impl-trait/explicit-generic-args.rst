tests/ui/impl-trait/explicit-generic-args-with-impl-trait/explicit-generic-args.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn foo<T: ?Sized>(_f: impl AsRef<T>) {}

fn main() {
    foo::<str>("".to_string());
}


