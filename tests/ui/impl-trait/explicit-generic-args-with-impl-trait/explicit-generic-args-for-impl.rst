tests/ui/impl-trait/explicit-generic-args-with-impl-trait/explicit-generic-args-for-impl.rs
===========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T: ?Sized>(_f: impl AsRef<T>) {}

fn main() {
    foo::<str, String>("".to_string()); //~ ERROR E0107
}


