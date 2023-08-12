tests/ui/borrowck/borrowck-pat-reassign-no-binding.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let mut x = None;
    match x {
      None => {
        // It is ok to reassign x here, because there is in
        // fact no outstanding loan of x!
        x = Some(0);
      }
      Some(_) => { }
    }
    assert_eq!(x, Some(0));
}


