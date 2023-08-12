src/tools/rustfmt/tests/target/issue-3741.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum PublishedFileVisibility {
    Public = sys::ERemoteStoragePublishedFileVisibility_k_ERemoteStoragePublishedFileVisibilityPublic as i32,
    FriendsOnly = sys::ERemoteStoragePublishedFileVisibility_k_ERemoteStoragePublishedFileVisibilityFriendsOnly as i32,
    Private = sys::ERemoteStoragePublishedFileVisibility_k_ERemoteStoragePublishedFileVisibilityPrivate as i32,
}


