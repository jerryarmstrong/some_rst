src/tools/miri/tests/pass/static_mut.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static mut FOO: i32 = 42;
static BAR: Foo = Foo(unsafe { &FOO as *const _ });

#[allow(dead_code)]
struct Foo(*const i32);

unsafe impl Sync for Foo {}

fn main() {
    unsafe {
        assert_eq!(*BAR.0, 42);
        FOO = 5;
        assert_eq!(FOO, 5);
        assert_eq!(*BAR.0, 5);
    }
}


