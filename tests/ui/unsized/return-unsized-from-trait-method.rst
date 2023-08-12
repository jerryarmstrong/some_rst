tests/ui/unsized/return-unsized-from-trait-method.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // regression test for #26376

trait Foo {
    fn foo(&self) -> [u8];
}

fn foo(f: Option<&dyn Foo>) {
    if let Some(f) = f {
        let _ = f.foo();
        //~^ ERROR cannot move a value of type `[u8]`
    }
}

fn main() { foo(None) }


