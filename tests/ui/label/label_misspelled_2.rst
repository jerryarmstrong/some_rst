tests/ui/label/label_misspelled_2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(unused_labels)]

fn main() {
    'a: for _ in 0..1 {
        break 'a;
    }
    'b: for _ in 0..1 {
        break b; //~ ERROR cannot find value `b` in this scope
    }
    c: for _ in 0..1 { //~ ERROR malformed loop label
        break 'c;
    }
    d: for _ in 0..1 { //~ ERROR malformed loop label
        break d; //~ ERROR cannot find value `d` in this scope
    }
}


