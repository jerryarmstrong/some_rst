src/tools/clippy/tests/ui/unit_return_expecting_ord.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::unit_return_expecting_ord)]
#![allow(clippy::needless_return)]
#![allow(clippy::unused_unit)]
#![feature(is_sorted)]

struct Struct {
    field: isize,
}

fn double(i: isize) -> isize {
    i * 2
}

fn unit(_i: isize) {}

fn main() {
    let mut structs = vec![Struct { field: 2 }, Struct { field: 1 }];
    structs.sort_by_key(|s| {
        double(s.field);
    });
    structs.sort_by_key(|s| double(s.field));
    structs.is_sorted_by_key(|s| {
        double(s.field);
    });
    structs.is_sorted_by_key(|s| {
        if s.field > 0 {
            ()
        } else {
            return ();
        }
    });
    structs.sort_by_key(|s| {
        return double(s.field);
    });
    structs.sort_by_key(|s| unit(s.field));
}


