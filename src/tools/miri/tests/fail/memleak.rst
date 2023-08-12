src/tools/miri/tests/fail/memleak.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@error-pattern: the evaluated program leaked memory
//@normalize-stderr-test: ".*│.*" -> "$$stripped$$"

fn main() {
    std::mem::forget(Box::new(42));
}


