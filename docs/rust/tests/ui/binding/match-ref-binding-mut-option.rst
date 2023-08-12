tests/ui/binding/match-ref-binding-mut-option.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let mut v = Some(22);
    match v {
      None => {}
      Some(ref mut p) => { *p += 1; }
    }
    assert_eq!(v, Some(23));
}


