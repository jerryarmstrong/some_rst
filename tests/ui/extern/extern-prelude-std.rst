tests/ui/extern/extern-prelude-std.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

mod foo {
    pub fn test() {
        let x = std::cmp::min(2, 3);
        assert_eq!(x, 2);
    }
}

fn main() {
    foo::test();
}


