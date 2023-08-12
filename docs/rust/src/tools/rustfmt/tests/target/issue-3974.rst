src/tools/rustfmt/tests/target/issue-3974.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn emulate_foreign_item() {
    match link_name {
        // A comment here will duplicate the attribute
        #[rustfmt::skip]
        | "pthread_mutexattr_init"
        | "pthread_mutexattr_settype"
        | "pthread_mutex_init"
        => {}
    }
}


