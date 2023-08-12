tests/ui/extern/auxiliary/no-mangle-associated-fn.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

struct Bar;

impl Bar {
    #[no_mangle]
    fn bar() -> u8 {
        2
    }
}

trait Foo {
    fn baz() -> u8;
}

impl Foo for Bar {
    #[no_mangle]
    fn baz() -> u8 {
        3
    }
}


