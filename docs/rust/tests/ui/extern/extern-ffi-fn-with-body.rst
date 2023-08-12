tests/ui/extern/extern-ffi-fn-with-body.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn foo() -> i32 { //~ ERROR incorrect function inside `extern` block
        return 0;
    }
}

extern "C" fn bar() -> i32 {
    return 0;
}

fn main() {}


