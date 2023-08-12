tests/ui/binding/expr-match-generic-unique2.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn test_generic<T: Clone, F>(expected: T, eq: F) where F: FnOnce(T, T) -> bool {
    let actual: T = match true {
        true => expected.clone(),
        _ => panic!("wat")
    };
    assert!(eq(expected, actual));
}

fn test_vec() {
    fn compare_box(v1: Box<isize>, v2: Box<isize>) -> bool { return v1 == v2; }
    test_generic::<Box<isize>, _>(Box::new(1), compare_box);
}

pub fn main() { test_vec(); }


