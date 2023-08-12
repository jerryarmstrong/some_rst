tests/ui/extern/issue-36122-accessing-externed-dst.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    extern "C" {
        static symbol: [usize]; //~ ERROR: the size for values of type
    }
    println!("{}", symbol[0]);
}


