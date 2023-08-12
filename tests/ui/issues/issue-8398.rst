tests/ui/issues/issue-8398.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

pub trait Writer {
    fn write(&mut self, b: &[u8]) -> Result<(), ()>;
}

fn foo(a: &mut dyn Writer) {
    a.write(&[]).unwrap();
}

pub fn main(){}


