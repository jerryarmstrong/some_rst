src/tools/miri/tests/fail/panic/double_panic.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@error-pattern: the program aborted
//@normalize-stderr-test: "\| +\^+" -> "| ^"
//@normalize-stderr-test: "unsafe \{ libc::abort\(\) \}|crate::intrinsics::abort\(\);" -> "ABORT();"

struct Foo;
impl Drop for Foo {
    fn drop(&mut self) {
        panic!("second");
    }
}
fn main() {
    let _foo = Foo;
    panic!("first");
}


