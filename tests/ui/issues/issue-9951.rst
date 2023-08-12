tests/ui/issues/issue-9951.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![allow(unused_variables)]

trait Bar {
  fn noop(&self);
}
impl Bar for u8 {
  fn noop(&self) {}
}

fn main() {
    let (a, b) = (&5u8 as &dyn Bar, &9u8 as &dyn Bar);
    let (c, d): (&dyn Bar, &dyn Bar) = (a, b);

    let (a, b) = (Box::new(5u8) as Box<dyn Bar>, Box::new(9u8) as Box<dyn Bar>);
    let (c, d): (&dyn Bar, &dyn Bar) = (&*a, &*b);

    let (c, d): (&dyn Bar, &dyn Bar) = (&5, &9);
}


