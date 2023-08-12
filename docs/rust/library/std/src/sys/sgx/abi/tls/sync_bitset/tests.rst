library/std/src/sys/sgx/abi/tls/sync_bitset/tests.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::*;

fn test_data(bitset: [usize; 2], bit_indices: &[usize]) {
    let set = SyncBitset([AtomicUsize::new(bitset[0]), AtomicUsize::new(bitset[1])]);
    assert_eq!(set.iter().collect::<Vec<_>>(), bit_indices);
    for &i in bit_indices {
        assert!(set.get(i));
    }
}

#[test]
fn iter() {
    test_data([0b0110_1001, 0], &[0, 3, 5, 6]);
    test_data([0x8000_0000_0000_0000, 0x8000_0000_0000_0001], &[63, 64, 127]);
    test_data([0, 0], &[]);
}

#[test]
fn set_get_clear() {
    let set = SYNC_BITSET_INIT;
    let key = set.set().unwrap();
    assert!(set.get(key));
    set.clear(key);
    assert!(!set.get(key));
}


