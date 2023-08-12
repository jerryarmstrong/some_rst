tests/ui/macros/issue-5060.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
macro_rules! print_hd_tl {
    ($field_hd:ident, $($field_tl:ident),+) => ({
        print!("{}", stringify!($field_hd));
        print!("::[");
        $(
            print!("{}", stringify!($field_tl));
            print!(", ");
        )+
        print!("]\n");
    })
}

pub fn main() {
    print_hd_tl!(x, y, z, w)
}


