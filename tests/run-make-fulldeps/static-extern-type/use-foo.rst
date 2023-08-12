tests/run-make-fulldeps/static-extern-type/use-foo.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

extern "C" {
    type Foo;
    static FOO: Foo;
    fn bar(foo: *const Foo) -> u8;
}

fn main() {
    unsafe {
        let foo = &FOO;
        assert_eq!(bar(foo), 42);
    }
}


