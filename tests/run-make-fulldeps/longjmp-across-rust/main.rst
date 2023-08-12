tests/run-make-fulldeps/longjmp-across-rust/main.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "foo", kind = "static")]
extern "C" {
    fn test_start(f: extern "C" fn());
    fn test_end();
}

fn main() {
    unsafe {
        test_start(test_middle);
    }
}

struct A;

impl Drop for A {
    fn drop(&mut self) {}
}

extern "C" fn test_middle() {
    let _a = A;
    foo();
}

fn foo() {
    let _a = A;
    unsafe {
        test_end();
    }
}


