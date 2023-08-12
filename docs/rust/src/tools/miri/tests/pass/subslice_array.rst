src/tools/miri/tests/pass/subslice_array.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bar(a: &'static str, b: &'static str) -> [&'static str; 4] {
    [a, b, b, a]
}

fn main() {
    let out = bar("baz", "foo");
    let [a, xs @ .., d] = out;
    assert_eq!(a, "baz");
    assert_eq!(xs, ["foo", "foo"]);
    assert_eq!(d, "baz");
}


