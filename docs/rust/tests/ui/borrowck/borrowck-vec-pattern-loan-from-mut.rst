tests/ui/borrowck/borrowck-vec-pattern-loan-from-mut.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a() {
    let mut v = vec![1, 2, 3];
    let vb: &mut [isize] = &mut v;
    match vb {
        &mut [_a, ref tail @ ..] => {
            v.push(tail[0] + tail[1]); //~ ERROR cannot borrow
        }
        _ => {}
    };
}

fn main() {}


