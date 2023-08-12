tests/ui/abi/extern/extern-call-direct.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test direct calls to extern fns.


extern "C" fn f(x: usize) -> usize { x * 2 }

pub fn main() {
    let x = f(22);
    assert_eq!(x, 44);
}


