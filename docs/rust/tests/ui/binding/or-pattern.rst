tests/ui/binding/or-pattern.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

enum blah { a(isize, isize, #[allow(unused_tuple_struct_fields)] usize), b(isize, isize), c, }

fn or_alt(q: blah) -> isize {
    match q { blah::a(x, y, _) | blah::b(x, y) => { return x + y; } blah::c => { return 0; } }
}

pub fn main() {
    assert_eq!(or_alt(blah::c), 0);
    assert_eq!(or_alt(blah::a(10, 100, 0)), 110);
    assert_eq!(or_alt(blah::b(20, 200)), 220);
}


