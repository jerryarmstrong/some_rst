tests/ui/borrowck/borrowck-assign-to-subfield.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    struct A {
        a: isize,
        w: B,
    }
    struct B {
        a: isize
    }
    let mut p = A {
        a: 1,
        w: B {a: 1},
    };

    // even though `x` is not declared as a mutable field,
    // `p` as a whole is mutable, so it can be modified.
    p.a = 2;

    // this is true for an interior field too
    p.w.a = 2;
}


