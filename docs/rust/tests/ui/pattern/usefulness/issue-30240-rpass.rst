tests/ui/pattern/usefulness/issue-30240-rpass.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn main() {
    let &ref a = &[0i32] as &[_];
    assert_eq!(a, &[0i32] as &[_]);

    let &ref a = "hello";
    assert_eq!(a, "hello");

    match "foo" {
        "fool" => unreachable!(),
        "foo" => {},
        ref _x => unreachable!()
    }
}


