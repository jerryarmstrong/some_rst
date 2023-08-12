src/tools/miri/tests/pass/from_utf8.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _val = ::std::str::from_utf8(b"a");
}


