tests/pretty/issue-68710-field-attr-proc-mac-lost.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

fn main() {}

struct C {
    field: u8,
}

#[allow()]
const C: C =
    C {
        #[cfg(debug_assertions)]
        field: 0,

        #[cfg(not(debug_assertions))]
        field: 1,
    };


