src/tools/miri/tests/extern-so/fail/function_not_in_so.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@only-target-linux
//@only-on-host
//@normalize-stderr-test: "OS `.*`" -> "$$OS"

extern "C" {
    fn foo();
}

fn main() {
    unsafe {
        foo(); //~ ERROR: unsupported operation: can't call foreign function `foo`
    }
}


