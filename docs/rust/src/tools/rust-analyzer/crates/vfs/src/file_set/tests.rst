src/tools/rust-analyzer/crates/vfs/src/file_set/tests.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::*;

#[test]
fn path_prefix() {
    let mut file_set = FileSetConfig::builder();
    file_set.add_file_set(vec![VfsPath::new_virtual_path("/foo".into())]);
    file_set.add_file_set(vec![VfsPath::new_virtual_path("/foo/bar/baz".into())]);
    let file_set = file_set.build();

    let mut vfs = Vfs::default();
    vfs.set_file_contents(VfsPath::new_virtual_path("/foo/src/lib.rs".into()), Some(Vec::new()));
    vfs.set_file_contents(
        VfsPath::new_virtual_path("/foo/src/bar/baz/lib.rs".into()),
        Some(Vec::new()),
    );
    vfs.set_file_contents(
        VfsPath::new_virtual_path("/foo/bar/baz/lib.rs".into()),
        Some(Vec::new()),
    );
    vfs.set_file_contents(VfsPath::new_virtual_path("/quux/lib.rs".into()), Some(Vec::new()));

    let partition = file_set.partition(&vfs).into_iter().map(|it| it.len()).collect::<Vec<_>>();
    assert_eq!(partition, vec![2, 1, 1]);
}

#[test]
fn name_prefix() {
    let mut file_set = FileSetConfig::builder();
    file_set.add_file_set(vec![VfsPath::new_virtual_path("/foo".into())]);
    file_set.add_file_set(vec![VfsPath::new_virtual_path("/foo-things".into())]);
    let file_set = file_set.build();

    let mut vfs = Vfs::default();
    vfs.set_file_contents(VfsPath::new_virtual_path("/foo/src/lib.rs".into()), Some(Vec::new()));
    vfs.set_file_contents(
        VfsPath::new_virtual_path("/foo-things/src/lib.rs".into()),
        Some(Vec::new()),
    );

    let partition = file_set.partition(&vfs).into_iter().map(|it| it.len()).collect::<Vec<_>>();
    assert_eq!(partition, vec![1, 1, 0]);
}


