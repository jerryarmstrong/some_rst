tests/ui/borrowck/borrowck-anon-fields-struct.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we are able to distinguish when loans borrow different
// anonymous fields of a tuple vs the same anonymous field.

struct Y(usize, usize);

fn distinct_variant() {
    let mut y = Y(1, 2);

    let a = match y {
        Y(ref mut a, _) => a
    };

    let b = match y {
        Y(_, ref mut b) => b
    };

    *a += 1;
    *b += 1;
}

fn same_variant() {
    let mut y = Y(1, 2);

    let a = match y {
        Y(ref mut a, _) => a
    };

    let b = match y {
        Y(ref mut b, _) => b //~ ERROR cannot borrow
    };

    *a += 1;
    *b += 1;
}

fn main() {
}


