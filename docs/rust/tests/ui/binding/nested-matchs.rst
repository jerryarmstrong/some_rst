tests/ui/binding/nested-matchs.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)] // under NLL we get warning about `bar` below
fn baz() -> ! { panic!(); }

fn foo() {
    match Some::<isize>(5) {
      Some::<isize>(_x) => {
        let mut bar;
        match None::<isize> { None::<isize> => { bar = 5; } _ => { baz(); } }
        println!("{}", bar);
      }
      None::<isize> => { println!("hello"); }
    }
}

pub fn main() { foo(); }


