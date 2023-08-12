tests/ui/self/string-self-append.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    // Make sure we properly handle repeated self-appends.
    let mut a: String = "A".to_string();
    let mut i = 20;
    let mut expected_len = 1;
    while i > 0 {
        println!("{}", a.len());
        assert_eq!(a.len(), expected_len);
        a = format!("{}{}", a, a);
        i -= 1;
        expected_len *= 2;
    }
}


