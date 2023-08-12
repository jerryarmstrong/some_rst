tests/run-make-fulldeps/issue64319/foo.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn foo() {
    bar::<usize>();
}

pub fn bar<T>() {
    baz();
}

fn baz() {}


