tests/ui/traits/default-method/macro.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


trait Foo {
    fn bar(&self) -> String {
        format!("test")
    }
}

enum Baz {
    Quux
}

impl Foo for Baz {
}

pub fn main() {
    let q = Baz::Quux;
    assert_eq!(q.bar(), "test".to_string());
}


