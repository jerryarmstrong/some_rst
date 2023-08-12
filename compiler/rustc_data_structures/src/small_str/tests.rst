compiler/rustc_data_structures/src/small_str/tests.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::*;

#[test]
fn empty() {
    let s = SmallStr::<1>::new();
    assert!(s.empty());
    assert_eq!("", s.as_str());
    assert!(!s.spilled());
}

#[test]
fn from_iter() {
    let s = ["aa", "bb", "cc"].iter().collect::<SmallStr<6>>();
    assert_eq!("aabbcc", s.as_str());
    assert!(!s.spilled());

    let s = ["aa", "bb", "cc", "dd"].iter().collect::<SmallStr<6>>();
    assert_eq!("aabbccdd", s.as_str());
    assert!(s.spilled());
}


