src/tools/rust-analyzer/crates/vfs/src/vfs_path/tests.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::*;

#[test]
fn virtual_path_extensions() {
    assert_eq!(VirtualPath("/".to_string()).name_and_extension(), None);
    assert_eq!(
        VirtualPath("/directory".to_string()).name_and_extension(),
        Some(("directory", None))
    );
    assert_eq!(
        VirtualPath("/directory/".to_string()).name_and_extension(),
        Some(("directory", None))
    );
    assert_eq!(
        VirtualPath("/directory/file".to_string()).name_and_extension(),
        Some(("file", None))
    );
    assert_eq!(
        VirtualPath("/directory/.file".to_string()).name_and_extension(),
        Some((".file", None))
    );
    assert_eq!(
        VirtualPath("/directory/.file.rs".to_string()).name_and_extension(),
        Some((".file", Some("rs")))
    );
    assert_eq!(
        VirtualPath("/directory/file.rs".to_string()).name_and_extension(),
        Some(("file", Some("rs")))
    );
}


