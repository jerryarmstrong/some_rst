tests/ui/codemap_tests/unicode_2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = ("a̐éö̲", 0u7); //~ ERROR invalid width
    let _ = ("아あ", 1i42); //~ ERROR invalid width
    let _ = a̐é; //~ ERROR cannot find
}


