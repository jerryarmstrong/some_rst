tests/ui/str/str-idx.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    let s: &str = "hello";
    let _: u8 = s[4]; //~ ERROR the type `str` cannot be indexed by `{integer}`
    let _ = s.get(4); //~ ERROR the type `str` cannot be indexed by `{integer}`
    let _ = s.get_unchecked(4); //~ ERROR the type `str` cannot be indexed by `{integer}`
    let _: u8 = s['c']; //~ ERROR the type `str` cannot be indexed by `char`
}


