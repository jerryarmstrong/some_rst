tests/ui/stability-attribute/stability-in-private-module.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = std::thread::thread_info::current_thread();
    //~^ERROR module `thread_info` is private
}


