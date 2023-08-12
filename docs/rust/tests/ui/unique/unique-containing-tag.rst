tests/ui/unique/unique-containing-tag.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

pub fn main() {
    enum t { t1(isize), t2(isize), }

    let _x: Box<_> = Box::new(t::t1(10));

    /*alt *x {
      t1(a) {
        assert_eq!(a, 10);
      }
      _ { panic!(); }
    }*/

    /*alt x {
      Box::new(t1(a) {
        assert_eq!(a, 10);
      })
      _ { panic!(); }
    }*/
}


