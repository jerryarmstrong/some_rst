tests/ui/resolve/export-fully-qualified.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // In this test baz isn't resolved when called as foo.baz even though
// it's called from inside foo. This is somewhat surprising and may
// want to change eventually.

mod foo {
    pub fn bar() { foo::baz(); } //~ ERROR failed to resolve: use of undeclared crate or module `foo`

    fn baz() { }
}

fn main() { }


