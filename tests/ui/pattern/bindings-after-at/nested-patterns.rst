tests/ui/pattern/bindings-after-at/nested-patterns.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


struct A { a: u8, b: u8 }

pub fn main() {
    match (A { a: 10, b: 20 }) {
        ref x @ A { ref a, b: 20 } => {
            assert_eq!(x.a, 10);
            assert_eq!(*a, 10);
        }
        A { b: ref _b, .. } => panic!(),
    }
}


