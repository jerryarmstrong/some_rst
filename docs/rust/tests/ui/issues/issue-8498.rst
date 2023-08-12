tests/ui/issues/issue-8498.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    match &[(Box::new(5),Box::new(7))] {
        ps => {
           let (ref y, _) = ps[0];
           assert_eq!(**y, 5);
        }
    }

    match Some(&[(Box::new(5),)]) {
        Some(ps) => {
           let (ref y,) = ps[0];
           assert_eq!(**y, 5);
        }
        None => ()
    }

    match Some(&[(Box::new(5),Box::new(7))]) {
        Some(ps) => {
           let (ref y, ref z) = ps[0];
           assert_eq!(**y, 5);
           assert_eq!(**z, 7);
        }
        None => ()
    }
}


