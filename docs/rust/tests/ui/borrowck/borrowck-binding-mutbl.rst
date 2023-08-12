tests/ui/borrowck/borrowck-binding-mutbl.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct F { f: Vec<isize> }

fn impure(_v: &[isize]) {
}

pub fn main() {
    let mut x = F {f: vec![3]};

    match x {
      F {f: ref mut v} => {
        impure(v);
      }
    }
}


