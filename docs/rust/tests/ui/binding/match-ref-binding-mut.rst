tests/ui/binding/match-ref-binding-mut.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_shorthand_field_patterns)]

struct Rec {
    f: isize
}

fn destructure(x: &mut Rec) {
    match *x {
      Rec {f: ref mut f} => *f += 1
    }
}

pub fn main() {
    let mut v = Rec {f: 22};
    destructure(&mut v);
    assert_eq!(v.f, 23);
}


