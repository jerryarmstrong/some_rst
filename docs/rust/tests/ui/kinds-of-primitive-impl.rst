tests/ui/kinds-of-primitive-impl.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl u8 {
//~^ error: cannot define inherent `impl` for primitive types
    pub const B: u8 = 0;
}

impl str {
//~^ error: cannot define inherent `impl` for primitive types
    fn foo() {}
    fn bar(self) {}
}

impl char {
//~^ error: cannot define inherent `impl` for primitive types
    pub const B: u8 = 0;
    pub const C: u8 = 0;
    fn foo() {}
    fn bar(self) {}
}

struct MyType;
impl &MyType {
//~^ error: cannot define inherent `impl` for primitive types
    pub fn for_ref(self) {}
}

fn main() {}


