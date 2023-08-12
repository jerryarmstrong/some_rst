tests/ui/borrowck/borrowck-slice-pattern-element-loan-rpass.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn mut_head_tail<'a, A>(v: &'a mut [A]) -> Option<(&'a mut A, &'a mut [A])> {
    match *v {
        [ref mut head, ref mut tail @ ..] => {
            Some((head, tail))
        }
        [] => None
    }
}

fn main() {
    let mut v = [1,2,3,4];
    match mut_head_tail(&mut v) {
        None => {},
        Some((h,t)) => {
            *h = 1000;
            t.reverse();
        }
    }
}


