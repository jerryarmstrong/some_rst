compiler/rustc_incremental/src/persist/fs/tests.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::*;

#[test]
fn test_all_except_most_recent() {
    assert_eq!(
        all_except_most_recent(vec![
            (UNIX_EPOCH + Duration::new(4, 0), PathBuf::from("4"), None),
            (UNIX_EPOCH + Duration::new(1, 0), PathBuf::from("1"), None),
            (UNIX_EPOCH + Duration::new(5, 0), PathBuf::from("5"), None),
            (UNIX_EPOCH + Duration::new(3, 0), PathBuf::from("3"), None),
            (UNIX_EPOCH + Duration::new(2, 0), PathBuf::from("2"), None),
        ])
        .keys()
        .cloned()
        .collect::<FxHashSet<PathBuf>>(),
        [PathBuf::from("1"), PathBuf::from("2"), PathBuf::from("3"), PathBuf::from("4"),]
            .into_iter()
            .collect::<FxHashSet<PathBuf>>()
    );

    assert_eq!(
        all_except_most_recent(vec![]).keys().cloned().collect::<FxHashSet<PathBuf>>(),
        FxHashSet::default()
    );
}

#[test]
fn test_timestamp_serialization() {
    for i in 0..1_000u64 {
        let time = UNIX_EPOCH + Duration::new(i * 1_434_578, (i as u32) * 239_000);
        let s = timestamp_to_string(time);
        assert_eq!(Ok(time), string_to_timestamp(&s));
    }
}

#[test]
fn test_find_source_directory_in_iter() {
    let already_visited = FxHashSet::default();

    // Find newest
    assert_eq!(
        find_source_directory_in_iter(
            [
                PathBuf::from("crate-dir/s-3234-0000-svh"),
                PathBuf::from("crate-dir/s-2234-0000-svh"),
                PathBuf::from("crate-dir/s-1234-0000-svh")
            ]
            .into_iter(),
            &already_visited
        ),
        Some(PathBuf::from("crate-dir/s-3234-0000-svh"))
    );

    // Filter out "-working"
    assert_eq!(
        find_source_directory_in_iter(
            [
                PathBuf::from("crate-dir/s-3234-0000-working"),
                PathBuf::from("crate-dir/s-2234-0000-svh"),
                PathBuf::from("crate-dir/s-1234-0000-svh")
            ]
            .into_iter(),
            &already_visited
        ),
        Some(PathBuf::from("crate-dir/s-2234-0000-svh"))
    );

    // Handle empty
    assert_eq!(find_source_directory_in_iter([].into_iter(), &already_visited), None);

    // Handle only working
    assert_eq!(
        find_source_directory_in_iter(
            [
                PathBuf::from("crate-dir/s-3234-0000-working"),
                PathBuf::from("crate-dir/s-2234-0000-working"),
                PathBuf::from("crate-dir/s-1234-0000-working")
            ]
            .into_iter(),
            &already_visited
        ),
        None
    );
}


