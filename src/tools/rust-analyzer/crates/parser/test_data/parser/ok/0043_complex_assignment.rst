src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0043_complex_assignment.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust-analyzer/issues/674

struct Repr { raw: [u8; 1] }

fn abc() {
    Repr { raw: [0] }.raw[0] = 0;
    Repr{raw:[0]}();
}


