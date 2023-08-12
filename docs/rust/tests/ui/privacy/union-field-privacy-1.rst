tests/ui/privacy/union-field-privacy-1.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m {
    pub union U {
        pub a: u8,
        pub(super) b: u8,
        c: u8,
    }
}

fn main() { unsafe {
    let u = m::U { a: 0 }; // OK
    let u = m::U { b: 0 }; // OK
    let u = m::U { c: 0 }; //~ ERROR field `c` of union `U` is private

    let m::U { a } = u; // OK
    let m::U { b } = u; // OK
    let m::U { c } = u; //~ ERROR field `c` of union `U` is private
}}


