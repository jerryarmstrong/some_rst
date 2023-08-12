tests/run-make-fulldeps/extern-fn-with-packed-struct/test.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(C, packed)]
#[derive(Copy, Clone, Debug, PartialEq)]
struct Foo {
    a: i8,
    b: i16,
    c: i8,
}

#[link(name = "test", kind = "static")]
extern "C" {
    fn foo(f: Foo) -> Foo;
}

fn main() {
    unsafe {
        let a = Foo { a: 1, b: 2, c: 3 };
        let b = foo(a);
        assert_eq!(a, b);
    }
}


