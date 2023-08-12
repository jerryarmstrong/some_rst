tests/ui/closures/old-closure-arg-call-as.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_snake_case)]

fn asBlock<F>(f: F) -> usize where F: FnOnce() -> usize {
   return f();
}

pub fn main() {
   let x = asBlock(|| 22);
   assert_eq!(x, 22);
}


